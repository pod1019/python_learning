'''集合的交集、并集、差集、对称差集'''
a = {1,3,'hello'}
b = {'jack','hello','dump'}
c = {1,3}

# 交集  取a中有的，且b中也有的
print(a&b)
print(a.intersection(b))


# 并集 a和b合并，去除重复的
print(a|b)
print(a.union(b))


# 差集 取a中有的，b中没有的
print(a-b)
print(a.difference(b))

# 对称差集    # 对称差集，把两个集合中都有的去掉
print(a^b)
print(a.symmetric_difference(b))

print(c.issubset(a))  # 判断c是不是a的子集
print(a.issuperset(c))  # 判断a是不是c的父集
print(a.isdisjoint(c))  # 判断a和c是否有交集


