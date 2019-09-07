import socket


def send_msg(udp_socket):
	"""发送数据"""	
	send_data = input("请输入要发送的数据:")
	dest_ip = input("请输入ip地址:")
	dest_port = int(input("请输入端口号:"))
	udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
	"""接收数据"""
	recv_data = udp_socket.recvfrom(1024)
	print("%s:%s" % (recv_data[1], recv_data[0].decode0("utf-8")))




def main():
	# 创建socket套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	# 绑定端口
	udp_socket.bind(("", 7788))
	# 循环来进行处理事情
	while True:
		print("-------xxx聊天器-------")
		print("1:发送消息")
		print("2:接收消息")
		print("0:退出系统")
		op = input("请输入功能:")
		if op == "1":
			# 发送
			send_msg(udp_socket)
		elif op == "2":
			# 接收并显示
			recv_msg(udp_socket)
		elif op == "0":
			break
		else:
 			print("输入错误请重新输入:")

if __name__ == "__main__":
	main()
