''''''
'''
 集合是无序的、元素不能重复且唯一的。
 实际上，集合底层是字典实现，集合的所有元素都是字典中的“键对象”，因此是不能重复的且唯一的。
'''
'''1、集合的创建,并使用add()方法添加元素'''
#  ① 使用{}创建集合对象，并使用 add()方法添加元素
s = {1,2,3}
print(s)
s.add(12)
print(s)

# ② 使用set()，将列表、元组等 可迭代 对象，转换成集合
# 如果原来数据有重复，则只保留一个
a = ['a','b','c','d']
b = set(a)
print(b)

#③remove()删除指定元素；
c = {10,20,30,40,50}
c.remove(20)
print(c)

#④clear()清空整个集合
d = {22,43,55}
d.clear()
print(d)


