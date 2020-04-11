'''
已知一个数列：1、1、2、3、5、8、13、。。。。的规律为从 3 开始的每一项都
等于其前两项的和，这是斐波那契数列。求满足规律的 100 以内的所以数据
'''
a = 0
b = 1
while b <100:
    print(b,end=",")
    a,b = b,a+b
print()

# 计算x的n次方
def mi(x,n):
    if n==0:
        return 1
    else:
        return x*mi(x, n-1)

x = 3
num = 6
print(mi(x,num))


