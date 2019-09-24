import multiprocessing
import os


def copy_file(file_name, old_folder_name, new_folder_name):
	"""完成文件的拷贝"""
	with open(old_folder_name+"/"+file_name, "rb") as f:
		content = f.read()
	with open(new_folder_name+"/"+file_name, "wb") as f:
		f.write(content)
		
	print("=======>模拟文件的拷贝:从%s------>到%s 文件名是%s" % (old_folder_name, new_folder_name, file_name))	


def main():
	# 获取用户要copy的文件夹的名字
	old_folder_name = input("请输入要copy文件夹的名字:")

	# 创建一个新的文件夹
	try:	
		new_folder_name = old_folder_name +"[复件]"
		os.mkdir(new_folder_name)
	except:
		pass

	# 获取文件夹中所有待copy的文件名字 os.listdir("路径")
	file_names = os.listdir(old_folder_name)	

	# 创建进程池
	po = multiprocessing.Pool(3)

	# 复制原文件夹中的文件，到新文件夹中去
	for file_name in file_names:
		po.apply_async(copy_file, args=(file_name, old_folder_name, new_folder_name))
	
	# 关闭进程池
	po.close()
	po.join()
	
	 	



if __name__ == "__main__":
	main()
