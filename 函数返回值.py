#测试函数返回值基本用法

def add(a, b):
    print("计算两个数的和：{0},{1},{2}".format(a,b,(a+b)))

add(3,5)

def test01():
    print("sxt")
    print("gaoqi")
    return  #return作用：1返回值，2结束函数执行；
    print("hello")

test01()

def test02(x,y,z):
    print([x*20,y*30,z*40])
    return [x*20,y*30,z*40]

test02(3,4,5)
print(end='\n\n\n')

print("_________________________测试函数也是对象_________________________")

#测试函数也是对象

def  test03():
    print("sxtsxt")

test03()
c = test03
c()

print(id(test03))
print(id(c))
print(type(c))
