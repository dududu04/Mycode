import socket 

def main():

	# 创建一个udp套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	# 输入要发送的数据
	send_data = input("请输入要发送的数据:")

	# 可以使用socket接收发数据
	udp_socket.sendto(send_data.encode("utf-8"), ('192.168.33.8080',8080))

	# 关闭套接字
	udp_socket.close()


if __name__=="__main__":
	main()
