import socket
import threading

def recv_msg(udp_socket):
	"""接收数据并显示"""
	while True:
		# 接收数据
		recv_data = udp_socket.recvfrom(1024)
		print(recv_data)


def send_msg(udp_socket):
	"""发送数据"""
	while True:
		# 发送数据
		send_data = input("输入要发送的数据:")
		udp_socket.sendto(send_data.encode("utf-8"),(dest_ip,dest_port))	



def main():
	"""完成udp聊天器的整体控制"""
	# 创建套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 绑定本地信息
	udp_socket.bind(("", 7890))
	
	# 获取对方的信息
	dest_ip = input("请输入对方的ip:")
	dest_port = int(input("请输入对方的port:"))	
	
	# 创建两个线程，去执行相应的功能
	t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
	t_send = threading.Threas(target=send_msg, args=(udp_socket, dest_ip, dest_port))
	
	# 启动线程
	t_recv.start()
	t_send.start()



if __name__ == "__main__":
	main()
