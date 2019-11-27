# -*- coding: utf-8 -*-
__author__ = "FTest"

#【操作】用列表和字典存储下表信息，并打印出表中工资高于 15000 的数据
r1 = dict(name="高小一",age=18,salary=35000,city="北京") #创建字典第一种方法
r2 = {"name":"高小六","age":"28","salary":"15000","city":"郑州"}#创建字典第二种方法
r3 = dict(name="高小二",age=20,salary=20000,city="上海")
r4 = dict(name="高小三",age=22,salary=10000,city="深圳")

tb = [r1,r2,r3,r4]

for x in tb:
    if float(x.get("salary"))>15000:
        print(x)
print()
print(tb)
