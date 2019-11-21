#1:变量作用域（全局变量和局部变量）
a = 100  #全局变量
def f1():
    global a  #如果要在函数内部改变全局变量的值，增加globle关键字声明
    print("全局变量：" + str(a))  # 打印全局变量
    a = 300

f1()
print("全局变量：" + str(a))

print("！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")


#2:全局变量和局部变量同名测试
b = 100
def f2():
    b = 3 #同名的局部变量
    print("局部变量：" + str(b))

f2()
print("全局变量：" + str(b)) # b仍然是100,没有变化，因为没有用globle在函数内部声明，所以b的值不变

print("__________________________________________________")
print(end='\n\n\n')


#3：输出局部变量和全局变量

c = 100
def f3(a,b,c):
    print(a,b,c)
    print(locals())  #打印输出局部变量
    print("#"*20)
    print(globals())  #打印输出全局变量

f3(2,3,4)
print(end='\n\n\n')

print("_____________________局部变量和全局变量效率测试_____________________________")
#3:局部变量和全局变量效率测试（局部变量的查询和访问速度比全局变量快，优先考虑使用，尤其是在循环的时候）
import math
import time

def test01():
    start = time.time()
    for i in range(10000000):
        math.sqrt(30) # math通过这个直接调用，就是全局变量
    end = time.time()
    print("全局变量耗时{0}".format((end-start)))


def test02():
    dd = math.sqrt  #直接把math下面的函数sqrt赋值给变量dd
    start = time.time()
    for i in range(10000000):
        dd(30)
    end = time.time()
    print("局部变量耗时{0}".format((end-start)))

test01()
test02()