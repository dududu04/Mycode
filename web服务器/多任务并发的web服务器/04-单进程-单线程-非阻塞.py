import socket
import time

def main():
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp_socket.bind(("", 7890))
	tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	# 设置套接字为非阻塞方式
	tcp_socket.setblocking(False)	
	tcp_socket.listen(128)
	client_socket_list = list()
	while True:
		time.sleep(0.5)
		try:
			new_socket, client_addr = tcp_socket.accept()
		except Exception as ret:
			print("没有客户端链接到服务器")
		else:
			print("有客户端链接")
			new_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
			new_socket.setblocking(False)
			client_socket_list.append(new_socket)
			print("列表为",client_socket_list)			
		for client_socket in client_socket_list:
			try:
				recv_data = client_socket.recv(1024)
			except Exception as ret:
				print("客户端没有发送数据")
			else:
				if recv_data:
					# 对方发送过来数据
					print("客户端发送数据:%s" % recv_data.decode("utf-8"))
				else:
					# 对方调用close导致recv返回
					client_socket_list.remove(client_socket)
					client_socket.close()
					print("客户端已经关闭")



if __name__ == "__main__":
	main()
