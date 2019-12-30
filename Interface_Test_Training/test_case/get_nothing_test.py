import unittest
import requests
from public import base
from ddt import ddt,data,unpack #ddt模块常用的3个方法
import xlrd

@ddt
class GetNothingTest(unittest.TestCase):
    '''GET无参数测试'''
    def setUp(self):
        endpoint = 'get'
        self.url = base.get_url(endpoint)

    @data(200,400,500,201)  #一个参数
    def test_1(self,result): #这里增加一个参数result，目的是把装饰器 @data 里的数据当作参数传到函数里
        '''校验状态码是否为200'''
        r = requests.get(self.url)
        status_code = r.status_code
        self.assertEqual(status_code,result)

    @data(('headers','Host','httpbin.org'),('headers','Accept-Encoding','gzip, deflate'))#多个参数：可以是列表、元组、也可以是字典；
    @unpack     #多个参数，需要把unpack引入进来
    # test_2设置三个参数，对应上面的value接收Host和Accept-Encodin；result接收返回结果httpbin.org和gzip, deflate
    def test_2(self,headers,value,result):
        '''校验header里host的值'''
        r = requests.get(self.url)
        resp = r.json()
        print(resp)
        # connectHost = resp['headers']['host']
        connectHost = resp[headers][value]
        self.assertEqual(connectHost,result)
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()