'''用 python 写个冒泡排序

'''
a = [1, 3, 10, 9, 21, 35, 4, 6]
s = range(1,len(a))[::-1] # 获得交换次数

print(list(s))

for i in s:
    for j in range(i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
    print("第 %s 轮交换后的数据是 %s" %(len(s)-i+1,a))

print(a)
