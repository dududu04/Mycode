import copy


a = [11,22]
b = copy.copy(a)

print("a的值为",a,"a的id为",id(a))
print("b的值为",b,"b的id为",id(b))

c = (11,22)
d = copy.copy(c)
e = copy.deepcopy(e)


print("c的值为",c,"c的id为",id(c))
print("d的值为",d,"d的id为",id(d))
print("e的值为",e,"e的id为",id(e))

print("由于元组的特性是不可变，用浅拷贝和深拷贝元组其实不会进行拷贝，仅仅是指向")
