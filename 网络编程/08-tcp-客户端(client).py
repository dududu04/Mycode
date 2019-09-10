import socket

def main():
	# 创建tcp套接字
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# 链接服务器
	server_ip = input("请输入要链接服务器的ip:")
	server_port = int(input("亲输入要链接的服务器的port:"))
	server_addr = (server_ip, server_port)
	tcp_socket.connect = (server_addr)

	# 发送数据/接收数据
	send_data = input("请输入要发送的数据:")
	tcp_client.send(send_data.encode("utf-8"))
	

	# 关闭套接字
	tcp_socket.close()



if __name__ == "__main__":
    main()
