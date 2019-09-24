


a = [11,22]
b = a
print("a的id是",id(a))
print("b的id是",id(b))



import copy

c = copy.copy(a)
d = copy.deepcopy(a)
print("c的id是",id(c))
print("d的id是",id(d))
print("a的值为",a)
print("b的值为",b)
print("c的值为",c)
print("d的值为",d)
a.append(33)
print("向a中append33后a的值为：",a)
print("向a中append33后b的值为：",b)
print("向a中append33后c的值为：",c)
print("向a中append33后d的值为：",d)
print("直接让一个b=a会让a和b指向同一个地址，而使用copy.copy(a)和copy.deepcopy(a)进行的浅拷贝复制会让c和d指向一个新的地址")
