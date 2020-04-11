# 统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1,-9, -4, -5, 8]

a = [1, 3, 5, 7, 0, -1,-9, -4, -5, 8]

# 方法1 生成新列表

b = [i for i in a if i > 0]
print("正数有：{}个".format(len(b)))

c = [i for i in a if i <0]
print("负数有：%d个" % len(c))

# 方法2 传统方法
m,n=0,0
for i in a:
    if i > 0:
        m+=1
    elif i < 0:
        n+=1
    else:
        pass
print("大于0的个数：%s" %m)
print("小于0的个数：%s" %n)

d = []
for i in a:
    if i>0:
        d.append(i)
print('d是：%s' %d)
