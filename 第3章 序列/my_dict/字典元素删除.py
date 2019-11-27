'''字典中元素的删除'''

'''
①可以使用 del() 方法；
②pop()删除指定 键值对，并返回对应的“值对象”
③clear()删除所有键值对；
'''

a = {'name':'小黑白','age':18, 'job':'QA','sex':'男','salary':9000.0}

del (a['name']) #①可以使用 del() 方法；
print(a)

b = a.pop('sex')  #②pop()删除指定 键值对，并返回对应的“值对象”
print(b)

c = {'name':'小明','age':20}
c.clear() #③clear()删除字典c的所有键值对；
print(c)

'''4. popitem() 随机删除和返回该键值对'''
d = {'name':'小6','age':30,'job':'PM'}
print(d.popitem())
print(d)