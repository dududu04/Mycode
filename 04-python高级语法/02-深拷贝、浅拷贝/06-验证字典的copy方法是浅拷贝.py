d = dict(name="zhangsan", age =27, children_ages=[11,22])

co = d.copy()


print(id(d))
print(id(co))

d["children_ages"].append(9)

print(d)
print(co)

