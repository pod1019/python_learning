''''''
'''1、序列解包可用于元组、列表、字典。  可以更方便给多个变量赋值'''

x,y,z = (20,30,60)
print('x的值是：{0}, y的值是：{1}, z的值是：{2}'.format(x,y,z))

(a,b,c) = (4,5,6)
print('a的值是：{0}, b的值是：{1}, c的值是：{2}'.format(a,b,c))

[d,e,f] = (8,10,9)
print('d的值是：{0}, e的值是：{1}, f的值是：{2}'.format(d,e,f))

'''
#2、序列解包用于字典时，默认是对“键”进行操作； 
#如果需要对键值对操作，则需要使用 items()；
#如果需要对“值”进行操作，则需要使用 values()；
'''
s = {'name':'小黑白','age':18, 'job':'QA'}
g,h,i = s #用a、b、c3个变量接收字典s的键
print(g)

name,age,job = s.items() # items()对 键值对 操作
print(age)

name,age,job = s.values() # values对 值 操作
print(name)