import copy

a = [11,22]

b = [33,44]

c = (a, b)

d = copy.copy(c)

e = copy.deepcopy(c)

print("c的值是",c,"c的id是",id(c))
print("d的值是",d,"d的id是",id(d))
print("e的值是",e,"e的id是",id(e))

a.append(33)
print("将a进行append(33)后,c的值",c)
print("将a进行append(33)后,d的值",d)
print("将a进行append(33)后,e的值",e)

print("如果元组内部都是不可变的元素，那么浅拷贝和深拷贝都不进行拷贝")
print("如果元组内部包含可变的元素，浅拷贝依然不拷贝，深拷贝会进行拷贝")
