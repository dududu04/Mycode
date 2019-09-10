import socket


def main():
	# 创建套接字
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# 绑定端口bind
	tcp_server_socket.bind(("", 7890))

	# 让默认套接字由主动变为被动listen
	tcp_server_socket.listen(128)

	while True:

		print("等待一个新的客户端的到来……")

		# 等待客户端的链接accept
		new_client_socket, client_addr = tcp_server_socket.accept()
		print("一个新的客户端已经到来%s" % str(client_addr))

		while True:
			# 接收客户端发送的数据
			recv_data = new_client_socket.recv(1024)
			print("客户端发送过来的请求是%s" % recv_data.decode("utf-8"))

			if recv-data:
				# 返回给客户端应答
				new_client_socket.send("hahaha".encode("utf-8"))
			else:
				break
		# 关闭套接字
		new_client_socket.close()

	tcp_server_socket.close()
		


if __name__ == "__main__":
	main()
