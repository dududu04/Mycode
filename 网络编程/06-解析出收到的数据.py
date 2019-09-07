import socket

def main():
	# 创建套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	# 绑定本地信息
	udp_socket.bind(("", 8080))

	# 接收数据
	recv_data = udp_socket.recvfrom(1024)
	# recv_data这个变量中存储的是一个元组(接收到的数据,(发送方的ip，发送方的端口))
	recv_msg = recv_data[0]
	send_addr = recv_data[1]

	# 打印接收到的数据
	print(recv_data)
	print("%s:%s" % (str(send_addr),recv_msg.decode("gbk")))

	# 关闭套接字
	udp_socket.close()

if __name__ == "__main__":
	main()
