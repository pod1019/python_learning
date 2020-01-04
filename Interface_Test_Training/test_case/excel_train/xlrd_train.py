import os
import xlrd
from datetime import date,datetime

newpath = os.chdir(r'D:\python_learning\Interface_Test_Training\test_case\excel_train')
filename = '100G测试资源（视频+教程）免费获取.xlsx'
file = os.path.join(os.getcwd(),filename)

'''一、打开文件'''
xl = xlrd.open_workbook(file)

'''二、获取sheet'''
# print(xl.sheet_names()) #获取所有sheet的名称
# print(xl.nsheets) # 获取一个xlsx文件有几个sheet，值就是几
#
# print(xl.sheet_by_name('目录'))  # 通过sheet名称获取sheet对象
# print(xl.sheet_by_index(0)) # 通过下标索引获取sheet对象

'''三、获取sheet内的汇总数据'''

table1 = xl.sheet_by_name('目录')
print(table1.name)
print(table1.nrows) # 获取所有行数
print(table1.ncols) # 获取所有列数

'''四、单元格批量读取'''
print(table1.row_values(0))


'''五、特定单元格读取'''
# 取值 以下几种方式都行，看自己习惯
# print(table1.cell_value(1,2)) #
# print(table1.cell(1,2).value) #
# print(table1.row(1)[2].value) # 第二行第三列
# print(table1.col(2)[1].value) # 第三列第二行
#
# # 取类型
# print(table1.cell_type(1,2))
# print(table1.cell(1,2).ctype)
# print(table1.row(1)[2].ctype)
# print(table1.col(2)[1].ctype)

'''六、常用技巧：(0,0)转换成A1'''
'''
read_excel函数封装：传递下标进来的时候，根据传的type值(比如传进来的type值是0、1、2、3、4 【0是空，1是字符换，2是数字类型，3是日期类型，4是布尔类型】)，
判断是啥类型，通过类型去转换。比如传进来的type值是2，就把2转换成对应的，即数字类型，传的type值是0，的话，转换成空，用单引号''
看的更明了'''
def read_excel(table,row,col):#传递excel对象table，以及行和列
    name = table.cell_value(row,col)
    type = table.cell_type(row,col)
    if type == 0:
        name = "''"
    elif type == 1:
        name = name
    elif type ==2 and name % 1 ==0:
        name = int(name)
    elif type == 3: #3是日期类型
        # 方法1 转换为日期时间
        # date_value = xlrd.xldate.xldate_as_datetime(name,0) #xldate_as_datetime(name,0)函数的参数 datemode一般都是0
        # name = date_value
        # 方法2 转换为元组
        data_value =  xlrd.xldate_as_tuple(name,0)
        name = datetime(*data_value).strftime('%Y-%m-%d %H:%M:%S')
    elif type == 4:
        name = True if name == 1 else False
    return name

'''七、获取表格内不同类型的name'''
print('----数字----')
print('当前单元格的值是：',table1.cell_value(1,1)) # 数字 2
print('当前单元格的值的类型是：',table1.cell_type(1,1)) #
print(read_excel(table1,1,1))

print('----空----')

print('当前单元格的值是：',table1.cell_value(0,1)) # 空 0
print('当前单元格的值的类型是：',table1.cell_type(0,1))
print(read_excel(table1,0,1))

print('----日期----')
print('当前单元格的值是：',table1.cell_value(0,7)) # 日期 3
print('当前单元格的值的类型是：',table1.cell_type(0,7))
print(read_excel(table1,0,7))

print('----布尔----')
print('当前单元格的值是：',table1.cell_value(0,8)) # 布尔 4
print('当前单元格的值的类型是：',table1.cell_type(0,8))
print(read_excel(table1,0,8))
print('s')