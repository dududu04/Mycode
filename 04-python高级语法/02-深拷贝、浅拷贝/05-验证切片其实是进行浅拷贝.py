import copy

a = [11,22]

b = [33,44]

c = [a,b]

d = c[:]

print("c的值是",c,"c的id是",id(c))
print("d的值是",d,"d的id是",id(d))

a.append(33)

print("将a进行append(33)后,c的值是",c)
print("将a进行append(33)后,d的值是",d)

print("切片属于浅拷贝")
