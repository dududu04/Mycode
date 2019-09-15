from gevent import monkey
import gevent
import time


# 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块补丁
monkey.patch_all()

def f1(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		time.sleep(0.5)

 
def f2(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		time.sleep(0.5)

def f3(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		time.sleep(0.5)
                       	            

print("---1---")
g1 = gevent.spawn(f1,5)
print("---2---")
g2 = gevent.spawn(f2,5)
print("---3---")
g3 = gevent.spawn(f3,5)
print("---4---")
g1.join()
g2.join()
g3.join()
