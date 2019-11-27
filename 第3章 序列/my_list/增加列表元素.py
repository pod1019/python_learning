
# 列表元素的增加和删除

a= [20,39]

a.append(100)# 向列表尾部追加元素

print(a)

b= [25]

print(id(b))

b= b+ [36]

print(id(b))# 通过如上测试id(b)，，两次id(b)的值不一致，我们发现变量 a 的地址发生了变化。也就是创建了新的列表对象

print(b)# 用运算符+ 操作,

a.extend(b)# 将目标列表的所有元素添加到本列表的尾部，属于原地操作，不创建新的列表对象

print(a)

# insert()插入元素

a.insert(2,'cn')  # 向下标为2的位置插入一个元素'cn'
print(a)

#乘法扩展
c = ['china',100.5]
d = c * 3
print(d)

