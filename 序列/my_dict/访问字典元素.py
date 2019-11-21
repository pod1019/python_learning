''''''
dict1 = {'name':'小白','age':18, 'job':'QA'}
'''1、通过 key（键）获得value（值）。如果键不存咋，则抛出异常'''
print(dict1['name']) # 通过键获得值
# print(dict1['sex'])  # 键不存在，抛出异常

'''2、通过get()方法获得“值”
优点是：指定键不存在，返回 None；也可以设定指定键不存在时默认返回的对象。推荐使用 get()获取“值对象”。
'''
print(dict1.get('name'))
print(dict1.get('sex','一个男人')) # 当指定的key不存在，默认返回一个值

'''3、列出所以键值对'''
print('字典dict1的所有键值对如下：',dict1.items())

'''4、①列出所有的键；  ②列出所有的值'''
print('字典dict1的所有键：',dict1.keys())
print('字典dict1的所有值：',dict1.values())

'''5、len()键值对的个数'''
print(len(dict1))

'''6、检测一个"键"是否在字典中'''
print('name' in dict1)