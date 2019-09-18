import socket
import re
import select


def service_client(new_socket, request):
	"""为这个客户端返回数据"""
	request_lines = request.splitlines()	
	print("")
	print(">>>>>"*20)
	print(request_lines)
	ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
	if ret:
		file_name = ret.group(1)  # 请求"127.0.0.1:7890/index.html" file_name为"/index.html"
		print("*"*50, file_name)	
		if file_name == "/":
			file_name = "/index.html"	
	
	try:
		f =  open("./html" + file_name, "rb")
	except:
		response = "HTTP/1.1 404 NOT FOUND\r\n"
		response += "\r\n"
		response += "------file:%s not found-----" % file_name
		new_socket.send(response.encode("utf-8"))
	else:
		html_content = f.read()
		f.close()
		response_body = html_content
		response_header = "HTTP/1.1 200 OK\r\n"
		response_header += "Content-Length:%d\r\n" % len(response_body)
		response_header += "\r\n"
		response = response_header.encode("utf-8") + response_body
		new_socket.send(response)



def main():
	"""用来完成整体的控制"""
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)	
	tcp_server_socket.bind(("",7890))
	tcp_server_socket.listen(128)
	tcp_server_socket.setblocking(False)
	# 创建一个epoll对象
	epl = select.epoll()	
	# 将监听套接字对应的fd注册到epoll中
	epl.register(tcp_server_socket.fileno(), select.EPOLLIN)
	fd_event_dict = dict()
	while True:
		fd_event_list = epl.poll()  # 默认会阻塞，直到 os监测到数据的到来 通过事件通知的方式 告诉这个程序，此时才会解阻塞
		# fd_event_list = [(fd,event),(套接字对于的文件描述符，这个文件描述符到底是什么事件 例如 可以调用recv接收等)]
		for fd,event in fd_event_list:
			if fd == tcp_server_socket.fileno():
				# 创建新的套接字
				new_socket, client_addr = tcp_server_socket.accept()
				epl.register(new_socket.fileno(), select.EPOLLIN)
				fd_event_dict[new_socket.fileno()] = new_socket
			elif event == select.EPOLLIN:
				recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
				if recv_data:
					service_client(fd_event_dict[fd], recv_data)
				else:
					fd_event_dict[fd].close()
					epl.unregister(fd)
					del fd_event_dict[fd]
	# 关闭监听套接字
	tcp_server_socket.close()


if __name__ == "__main__":
	main()
