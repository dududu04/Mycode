import socket 

def main():

	# 创建一个udp套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 获取对方的ip/port
	dest_ip = input("请输入ip地址:")
	dest_port = int(input("请输入对方的端口:"))

	# 输入要发送的数据
	send_data = input("请输入要发送的数据:")

	# 可以使用socket接收发数据
	udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))
	
	# 使用socket收数据
	recv_data = udp_socket.recvfrom(1024)

	# 打印收到数据
	print(recv_data[0].decode("gbk"))

	# 关闭套接字
	udp_socket.close()


if __name__=="__main__":
	main()
