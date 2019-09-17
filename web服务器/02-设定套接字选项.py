import socket


def service_client(new_socket):
	"""为这个客户端返回数据"""
	
	# 接收浏览器发送过来的请求，即http请求
	# GET / HTTP/1.1
	# ....
	request = new_socket.recv(1024)
	print(request)
	
	# 返回http格式的数据，给浏览器
	# 准备发送给浏览器的数据 --- header
	response = "HTTP/1.1 200 OK\r\n"
	response += "\r\n"
	# 准备发送给浏览器的数据 --- body
	response += "<h1>hahaha</h1>"
	new_socket.send(response.encode("utf-8"))
	
	# 关闭套接字
	new_socket.close()


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

	while True:
		# 等待新客户端的链接
		new_socket, client_addr = tcp_server_socket.accept()

		# 为这个客户端服务
		service_client(new_socket)
	# 关闭监听套接字
	tcp_server_socket.close()


if __name__ == "__main__":
	main()
