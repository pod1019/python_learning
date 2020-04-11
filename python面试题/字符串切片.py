# 字符串 "axbyczdj"，如果得到结果“abcd”
a = "axbyczdj"
#1、用切片：从开头到结尾，步长为2。
b = a[::2]
print('切片结果：',b)

# 2、传统思维
c = []
for i in range(len(a)):
    if i % 2 ==0:
        c.append(a[i])
print("传统方法结果是：","".join(c))




# # 字符串反转
# c = a[::-1]
# print(c)