import random
# 列表遍历
list1 = [2,30,40,60,12,9]
for i in list1:
    print(i)

# 复制列表所有的元素到新列表对象
list2 = list1  #只是将 list2 也指向了列表对象，也就是说 list2 和 list2 持有地址值是相同的，列表对象本 身的元素并没有复制。
print(list2)

list2 = [] + list1 # 用此方法，实现列表元素内容的复制：
print(list2)

"""#列表排序 修改原列表，不建新列表的排序"""
list1.sort() # 默认升序
print('-----',list1)

list1.reverse() #降序
print('使用reverse()方法降序后，list1是：',list1)

random.shuffle(list1)  # 打乱顺序random.shuffle()
print('使用random.shuffle()后，list1是：',list1)


"""建新列表的排序 
我们也可以通过内置函数 sorted()进行排序，这个方法返回新列表，不对原列表做修改。"""

list3 = [20,40,50,10,5]

list4 = sorted(list3) #升序

list5 = sorted(list3,reverse=True) #降序
print('list3是：',list3)
print('使用sorted()后，list4是',list4)
print('使用sorted(list3,reverse=True)后，list5是',list5)
