'''
已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：
[3, 5, 1, 7]
'''

a = [1, 3, 5, 7]

# insert 插入数据
a.insert(3,a[0]) # 在第三个位置插入a[0]这元素，也就是在第三个位置插入1，现在a变成了[1, 3, 5, 1, 7]
print(a[1:]) # 取列表a第一道最后一个，即得到[3, 5, 1, 7]