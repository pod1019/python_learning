import xlrd
'''
123'''
''''''
# 1.xlrd主要是用来读取excel文件
data = xlrd.open_workbook(r'abcd.xlsx') #打开xls文件
# data = xlrd.open_workbook('E:\\www\\abcd.xlsx') #打开xls文件

table = data.sheets()[0] #打开第一张表
nrows = table.nrows #获取表的行数
print(f'表的行数是：{nrows}')

for i in range(nrows):
    if i == 0:
        continue
    print(table.row_values(i))

#