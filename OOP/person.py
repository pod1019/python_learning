'''人 类型
'''
class Person:
    def __init__(self,name='', age='', gender=''):#给参数默认值的作用是：new对象的时候可以传参数，也可不传参数
        self.name = name
        self.age = age
        self.gender=gender
    def say(self,word): #self 定义的时候需要写出来
        print('{}的岁{} 说：{}'.format(self.age,self.name,word))

        # print(f'{self.age}的岁{self.name} 说：{word}') # 上一行在python3.6及以后也可以这么写。

p = Person()
p1 = Person('Tom',20)
p2 = Person('Jerry',22)

print(p1.name)
print(p2.name)

p1.say('今天天气真好！') #self在调用的时候，不需要写
p2.say('我想学Python！')