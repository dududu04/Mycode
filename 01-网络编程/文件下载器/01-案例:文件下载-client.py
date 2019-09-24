import socket


def main():
	tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 链接服务器
	server_ip = input("请输入要链接服务器的ip:")
	server_port = int(input("请输入要链接服务器的port:"))
	server_addr = (server_ip, server_port)
	tcp_client_socket.connect(server_addr)

	# 请输入要下载的文件名
	file_name = input("请输入要下载的文件名:")

	# 发送请求
	tcp_client_socket.send(file_name.encode("utf-8"))

	# 接收文件中的数据
	recv_data = tcp_client_socket.recv(1024*1024)	
	
	if recv_data:
		# 保存接收到的数据到一个文件中
		with open("[新]" + file_name, "wb") as f:
			f.write(recv_data)

	# 关闭套接字
	tcp_client_socket.close()


if __name__ == "__main__":
	main()
