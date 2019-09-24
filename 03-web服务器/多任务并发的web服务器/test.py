import socket
import re
import select


def service_client(new_socket, request):
	"""为这个客户端返回数据"""
	
	# 切割请求为一个列表
	request_lines = request.splitlines()	
	print("")
	print(">>>>>"*20)
	print(request_lines)
	# 提取请求的文件名 GET /index.html HTTP/1.1 get/post/put/del
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
		# 准备发送给浏览器的数据 --- body
		response_body = html_content
		# 准备发送给浏览器的数据 --- header
		response_header = "HTTP/1.1 200 OK\r\n"
		response_header += "Content-Length:%d\r\n" % len(response_body)
		response_header += "\r\n"
		response = response_header.encode("utf-8") + response_body
		# 将response发送
		new_socket.send(response)



def main():
	"""用来完成整体的控制"""
	# 创建套接字
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# 设置当服务器先close即服务器4次挥手之后资源能够立即释放，这样就保证了下次运行程序时，可以立即执行
	tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)	

	# 绑定
	tcp_server_socket.bind(("",7890))

	# 变为监听套接字
	tcp_server_socket.listen(128)
	
	# 创建epoll区域
	epl = select.epoll()

	# 将主进程登录进epoll
	epl.register(tcp_server_socket.fileno(), select.EPOLLIN)

	# 创建字典保存套接字
	new_socket_dict = dict()
	while True:
		fd_event_list = epl.poll()
		for fd,event in fd_event_list:
			if fd == tcp_server_socket.fileno():
				new_socket, client_addr = tcp_server_socket.accept()
				epl.register(new_socket.fileno(), select.EPOLLIN)
				new_socket_dict[new_socket.fileno()] = new_socket
			elif event  == select.EPOLLIN :	
				recv_data = new_socket_dict[fd].recv(1024).decode("utf-8")
				if recv_data:
					service_client(new_socket_dict[fd], recv_data)
				else:
					new_socket_dict[fd].close()
					epl.unregister(fd)
					del new_socket_dict[fd]

	# 关闭监听套接字
	tcp_server_socket.close()


if __name__ == "__main__":
	main()
