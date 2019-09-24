


num = 100
nums = [11, 22]
nums += [3]

def test():
	global num
	num += 100

def test2():
	global nums += [100, 200]


def test3():
	nums.append(33)


print(num)

test()

print(num)
print(nums)

test2()

print(nums)

test3()

print(nums)
