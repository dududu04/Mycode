from common import RECV_DATA_LIST
import common


def handle_data():
	"""模拟处理recv_msg模块接收的数据"""
	print("----->handle_data")
	for i in RECV_DATA_LIST:
		print(i)

	# 既然处理完成，那么将变量的HANDLE_FLAG设置为True，意味着处理完成
	# global HANDLE_FLAG
	common.HANDLE_FLAG = True




def test_handle_data():
	"""测试处理是否完成，变量是否设置为True"""
	print("----->test_handle_data")
	if common.HANDLE_FLAG:
		print("=====已经处理完成=====")
	else:
		print("=====未处理完成====")
