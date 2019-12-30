from public import Config
from public import HttpService
from public import read_excel
'''#函数封装'''
def get_url(EndPoint): # 用例中定义的endpoint都不一样，写在这里，怎么修改都不会影响用例，用例只要把传递参数过来
    host = Config.url()
    endpoint = EndPoint
    url = ''.join([host, endpoint])
    return url

def get_response(url,Method,**DataALL):
    resp = None
    if Method =='get':
        resp = HttpService.MyHTTP().get(url,**DataALL)
    elif Method == 'post':
        resp = HttpService.MyHTTP().post(url,**DataALL)
    return resp
def get_data(testfile,sheetname):
    '''
    datainfo =  read_excel.XLDatainfo(r'D:\python_learning\Interface_Test_Training\test_data\get_params_headers_test_data.xlsx')
    由于文件不是固定的，所有用文件名testfile代替代get_params_headers_test_data.xlsx
    '''
    datainfo =  read_excel.XLDatainfo(r'D:\python_learning\Interface_Test_Training\test_data\%s' %testfile)
    Data = datainfo.get_sheetinfo_by_name(sheetname)
    return Data