#测试浅拷贝，深拷贝
import copy

def testCopy():
    a = [10, 20, [5, 6]]
    b = copy.copy(a)
    print("a原值:",a)
    print("b原值:",b)

    b.append(30)
    b[2].append(7)
    print("浅拷贝后结果如下...................")
    print("a:",a)
    print("b:",b)

testCopy()

print("___________________________")

def testDeepCopy():
    a = [10, 20, [5, 6]]
    b = copy.copy(a)
    print("a原值:", a)
    print("b原值:", b)

    b.append(30)
    b[2].append(7)
    print(">>>>>深拷贝后结果如下...................")
    print("a:", a)
    print("b:", b)

testDeepCopy()