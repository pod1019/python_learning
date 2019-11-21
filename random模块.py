import random
number = input("请输入你要选择几注彩票：")
#每注号码由7个数字组成。前面六个为红色球，选号范围01-33，最后一位是蓝色球，选号范围01-16
#需求分析：
 #1、6个红色球，1-33，[1,33] random.sample([1,33],6)
 #2、1个蓝色球  1-16, random.randit(1,16)

red_balls = range(1,34)
lst = []
for r in red_balls:
    lst.append(str(r).zfill(2))

for i in range(int(number)):
    red = random.sample(lst,6)
    blue = str(random.randint(1,16)).zfill(2)
    red.sort()
    red = ','.join(red)
    print('红球',red,'蓝球',blue)


