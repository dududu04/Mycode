a = [11,22]
b = [33,44]



import copy

c = [a,b]
d = c
e = copy.copy(c)
f = copy.deepcopy(c)
print("c的id是",id(c),"c的值为",c)
print("d的id是",id(d),"d的值为",d)
print("e的id是",id(e),"e的值为",e)
print("f的id是",id(e),"f的值为",f)
a.append(33)
print("向a中append33后c的值为：",c)
print("向a中append33后d的值为：",d)
print("向a中append33后e的值为：",e)
print("向a中append33后f的值为：",f)


print("d=c使得两者指向的地址相同")
print("e=copy.copy(c)进行浅拷贝，使得e和c指向不同的地址，但他们内部存的a，b确指向相同的地址")
print("f=copy.deepcopy(c)进行深拷贝，不仅使f和c指向不同的地址，还会将内部列表进行拷贝")
