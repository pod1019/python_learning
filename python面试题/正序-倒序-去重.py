a = [1,3,6,9,7,3,4,6]
# 1 sort排序，正序
a.sort()
print(a)

# 2 sort 倒序
a.sort(reverse=True)
print(a)

# 3 去重
b = list(set(a))
print(b)