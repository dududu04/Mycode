import socket
import re


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
	
	# 将套接字变为非阻塞
	tcp_server_socket.setblocking(False)

	client_socket_list = list()
	while True:
		try:
			# 等待新客户端的链接
			new_socket, client_addr = tcp_server_socket.accept()
			
		except Exception as ret:
			pass
		else:			
			new_socket.setblocking(False)
			client_socket_list.append(new_socket)

		for client_socket in client_socket_list:
			try:
				recv_data = client_socket.recv(1024).decode("utf-8")
			except Exception as ret:
				pass
			else:
				if recv_data:
					service_client(client_socket, recv_data)
				else:
					client_socket_list.remove(client_socket)
					client_socket.close()
					

	# 关闭监听套接字
	tcp_server_socket.close()


if __name__ == "__main__":
	main()
