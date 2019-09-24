import threading
import time


g_nums = [11,22]


def test1(temp):
	temp.append(33)
	print("--------in test1 temp=%s-------" % str(temp))

def test2(temp):
	print("--------in test2 temp=%s-------" % str(temp))


def main():
	# target 指定将来这个线程去哪个函数执行代码
	# args 指定将来调用这个函数的时候 传递什么参数过去
	t1 = threading.Thread(target=test1, args=(g_nums,))
	t2 = threading.Thread(target=test2, args=(g_nums,))
	t1.start()
	time.sleep(1)

	t2.start()
	
	print("--------in main g_nums=%s-------" % str(g_nums))


if __name__ == "__main__":
	main()
