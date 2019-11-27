# 1、表格数据使用字典和列表存储，并实现访问

r1 = {'name':'小白','age':25,'salary':20000.0,'city':'北京'}
r2 = {'name':'小黑','age':30,'salary':15000.0,'city':'杭州'}
r3 = {'name':'小明','age':33,'salary':30000.0,'city':'上海'}

tb = [r1,r2,r3]

# 2、获取第二行的人的薪资
salary2 = tb[1].get('salary')
print(salary2)

# 3、打印表中所有的的薪资
'''
for i in len(tb): #报错 TypeError: 'int' object is not iterable。因为len(tb)的结果是一个int型
所以用range()函数包起来
'''
for i in range(len(tb)):
    salary1 = tb[i].get('salary')
    print(salary1)

# 4、打印表中所有数据
for i in range(len(tb)):
    print(tb[i].get('name'),tb[i].get('age'),tb[i].get('salary'),tb[i].get('city'))