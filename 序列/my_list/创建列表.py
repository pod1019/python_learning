# 列表创建

# 1、第一种方式
list1= [10,20,'QQ','中国']

# 2、用list()函数创建
list2= list('helle everybody!')

# 3、用list()函数和range()创建
list3= list(range(3,18,2))

# 4、推导式生成列表
list4= [x* 2 for x in range(10)]

print(f'列表1是:{list1},\r\n列表2是:{list2},\r\n列表3是:{list3}\r\n列表4是：{list4}')


# 多维列表
list5 = [
            ['小白',18,5000,'上海'],
            ['小黑',27,12000,'北京'],
            ['小红',32,28000,'郑州']
        ]

print(list5[1][0],list5[1][1],list5[1][2],list5[1][3])