import xlrd
class XLDatainfo(object):
    def __init__(self,path=''): # 初始化对象，并给一个参数path，文件路径
        self.xl = xlrd.open_workbook(path)

    def get_sheetinfo_by_name(self,name):
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_sheet_info()

    # 循环读取excel里的数据
    def get_sheet_info(self):
        infolist = [] #把excel文件每个sheet里的小的列表，放到这个大列表里
        for row in range(0,self.sheet.nrows): # 获取sheet的行数
            info = self.sheet.row_values(row) # 通过行，取值
            infolist.append(info) # 把取到的行的值，放到大列表中
        return infolist

if __name__=="__main__":
    datainfo = XLDatainfo(r'D:\python_learning\Interface_Test_Training\test_data\get_params_headers_test_data.xlsx') # new一个对象，并传递一个path进来
    alldata = datainfo.get_sheetinfo_by_name('AllData')  #alldata=datainfo.get_sheetinfo_by_name('TestData')
    print(alldata)