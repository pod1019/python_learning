import xlrd
import xlutils.copy
xl = xlrd.open_workbook('test.xlsx')

workbook = xlutils.copy.copy(xl) # 拷贝文件
worksheet = workbook.get_sheet(0) # 得到拷贝文件的sheet
worksheet.write(0,0,'changed') # 向特定格式，写入内容，即更改
workbook.save('xlutils.xls') # 保存文件。2个弊端：1.没有把格式和图片赋值过来；2、只支持保存成xls格式（用excel打不开，wps可以）