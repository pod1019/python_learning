#推导式练习
#  列表推导式
li = [x*2 for x in range(1,4)]

print (li)

cells = [(row,col) for row in range(1,10) for col in range(1,10)]
print (cells)

#字典推导式
my_text = "you are welcome, you are right,hello"
char_count = ({l:my_text.count(l) for l in my_text})
print (char_count)

#课后作业，使用普通的循环实现上面的推导式 统计字符出现的次数

#集合推导式
squared = {x**2 for x in (1,1,2)}
print (squared)
#生成器推导式(生成元组)
gen = ((i+2)**2 for i in range(10))

#print (tuple(list(gen)))

print (list(gen))
print (gen)



def add(a,b):
    print ("计算2个数之和：{0}+{1}={2}".format(a,b,(a+b)))
    return a+b

c = add(30,40)

print(add(30,40)*10)

