import xlsxwriter
import datetime
'''1、创建excel文件和sheet'''
workbook = xlsxwriter.Workbook('test.xlsx') #创建文件
worksheet = workbook.add_worksheet('test') #创建sheet，会清空原有文件内容
print(worksheet)
'''2、向特定单元格里写入内容'''
worksheet.write('A1','软件测试')
worksheet.write(1,0,'软件测试A2')


'''自定义格式、行设置、列设置'''
top = workbook.add_format({'border':1,'font_size':13,'bold':True,'align':'center','bg_color':'cccccc'})
worksheet.write('A3','软件测试A3',top)
worksheet.set_row(0,40,top) # 设置航属性，设置第1行的行高为40
worksheet.set_column('A:E',20,top)#设置列属性（A:E,表示A到E列）
'''写入数字和函数'''
worksheet.write(0,1,32) # 向第1行第2列，写入32
worksheet.write(1,1,35.5)
worksheet.write(2,1,'=sum(B1:B2)') #写入函数，=sum(B1:B2) excel里函数

'''写入日期'''
'''
worksheet.write(0,2,datetime.datetime.strptime('2017-11-11','%Y-%m-%d'))如果只写到这一步，写入的日期是一个数字
所以需要进行格式转换，workbook.add_format({'num_format':'yyyy-mm-dd'}
'''
worksheet.write(0,2,datetime.datetime.strptime('2017-11-11','%Y-%m-%d'),workbook.add_format({'num_format':'yyyy-mm-dd'}))

'''插入图片'''
# 1、最基本的插入方式
# worksheet.insert_image(0,4,'软件测试.jpg')
# 2、插入并设置一些属性
worksheet.insert_image(14,4,'软件测试.jpg',{'x_scale':0.2,'y_scale':0.2,'url':'www.baidu.com'})   #设置图片比例。也可以设置链接等

'''批量写入'''
# 从A15单元格开始写，第二个参数是个列表（元组也行）
worksheet.write_row('A15',[5,6,7,8])
# 列写入，从A16这个单元格开始写
worksheet.write_column('A16',[1,2,3,4])

'''合并单元格写入'''
worksheet.merge_range(4,0,5,2,'巧吧软件测试',top) # 前4个参数含义分别是：开始行，开始列，结束行，结束列


'''关闭文件流'''
workbook.close() # 必须要有此步骤，要不然看不到创建的excel文件