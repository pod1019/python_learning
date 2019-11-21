# -*- coding: utf-8 -*-
__author__ = "FTest"

#九九乘法表
for m in range(1,10):
    for n in range(1,m+1):
        print("{0}*{1}={2}".format(n,m,(n*m)),end="\t")
    print()

#一个循环体内可以嵌入另一个循环，一般称为“嵌套循环”，或者“多重循环”。
for x in range(5):
    for y in range(5):
        print(x,end="\t")
    print()


