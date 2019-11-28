import xlrd

'''1.xlrd主要是用来读取excel文件'''

'''打开一个workbook，即打开一个Excel文件'''

workbook = xlrd.open_workbook('./abcd.xlsx')

'''抓取所有sheet页的名称'''
worksheets = workbook.sheet_names()
print('Excel文件所有的sheet页名字是：{0}'.format(worksheets))

'''定位到某个sheet1'''
worksheet1 = workbook.sheet_by_name(u'借款列表')
print('worksheet1的值是：',worksheet1,'\r\n')

'''通过索引顺序获取'''
worksheet2 = workbook.sheets()[0]
#或者
worksheet3 = workbook.sheet_by_index(0)

'''遍历所有sheet对象'''
for worksheet_name in worksheets:
    worksheet = workbook.sheet_by_name(worksheet_name)
    print(worksheet)

'''遍历sheet1中所有行row'''
num_rows = worksheet1.nrows
for curr_row in range(num_rows):
    row = worksheet1.row_values(curr_row)
    print(curr_row,row)

'''遍历sheet1中所有的列col'''
num_cols = worksheet1.ncols
for curr_col in range(num_cols):
    col = worksheet1.col_values(curr_col)




for rown in range(num_rows):
    for coln in range(num_cols):
        pass
