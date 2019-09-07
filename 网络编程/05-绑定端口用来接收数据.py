import socket

def main():
	# 创建套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	# 绑定本地信息
	udp_socket.bind(("", 8080))

	# 接收数据
	recv_data = udp_socket.recvfrom(1024)	

	# 打印接收到的数据
	print(recv_data)

	# 关闭套接字
	udp_socket.close()

if __name__ == "__main__":
	main()
