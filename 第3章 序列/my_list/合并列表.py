'''
list1 = [1,2,3]
list2 = ['a','b','c','d','f'],把list1和list2合成list3，如下。用python实现
list3 = [(1,'a'),(2,'b'),(3,'c'),(1,'d'),(2,'f')]
'''
list1 = [1,2,3]
list2 = ['a','b','c','d','f']
list3 =[]
x=0
list2 = iter(list2 )
while True:
    if x == len(list1):
        x = 0
    try:
        list3.append((list1[x],next(list2)))
    except StopIteration:
        break
    x+=1     #x = x+1

print(list3)