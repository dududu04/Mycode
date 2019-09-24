import threading
import time

g_num = 0


def test1(temp):
	global g_num
	for i in range(temp):
		g_num += 1		
	print("--------in test1 g_num=%s-------" % g_num)

def test2(temp):
	global g_num
	for i in range(temp):
		g_num += 1		
	print("--------in test2 g_num=%s-------" % g_num)


def main():
	# target 指定将来这个线程去哪个函数执行代码
	# args 指定将来调用这个函数的时候 传递什么参数过去
	t1 = threading.Thread(target=test1, args=(1000000,))
	t2 = threading.Thread(target=test2, args=(1000000,))
	t1.start()
	t2.start()
	
	time.sleep(5)
	print("--------in main g_nums=%d-------" % g_num)


if __name__ == "__main__":
	main()
