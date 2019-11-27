''''''
'''

'''
r1 = {'name':'小白','age':18,'salary':30000,'city':'北京'}
r2 = {'name':'小黑','age':19,'salary':20000,'city':'上海'}
r3 = {'name':'小红','age':20,'salary':10000,'city':'深圳'}

tb = [r1,r2,r3]

for i in range(len(tb)):
    salary = tb[i].get('salary')
    if salary >15000:
        print('高于15000的工资有：{0}'.format(salary))
for i in range(len('ssss')):
    print(i)