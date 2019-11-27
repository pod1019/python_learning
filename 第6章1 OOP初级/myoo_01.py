import math


class Student:
    company = "SXT"
    count = 0 #类属性
    def __init__(self,name,score):
        self.name = name
        self.score = score
        Student.count +=1

    def say_score(self):
        print ("我的公司是：", Student.company)
        print (self.name,'的分数是：',self.score)

s1 = Student('张三',30)
s2 = Student('张111',44)
s1.say_score()
print ('一共创建{0}个student对象'.format(Student.count))

print()