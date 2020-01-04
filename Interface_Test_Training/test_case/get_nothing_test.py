import unittest
import requests
from public import base
from ddt import ddt,data,unpack #ddt模块常用的3个方法

testcasefile = 'get_nothing_test_data.xlsx'
AllData = base.get_data(testcasefile,'AllData') # 获取测试用例文件 testcasefile，并进一步取到该文件的sheet名，即AllData
TestData = base.get_data(testcasefile,'TestData')[1:] # 获取测试用例文件 testcasefile，并进一步取到该文件的sheet名，即T
print(TestData)
@ddt
class GetNothingTest(unittest.TestCase):
    '''GET无参数测试'''
    def setUp(self):
        self.endpoint = AllData[1][1]
        self.RequestMethod = AllData[1][2]
        self.RequestData = AllData[1][3]
        self.url = base.get_url(self.endpoint)
    # @data(('headers','Host','httpbin.org'),('headers','Accept-Encoding','gzip, deflate'))#多个参数：可以是列表、元组、也可以是字典；
    @data(*TestData)
    @unpack     #多个参数，需要把unpack引入进来
    # test_2设置三个参数，对应上面的key接收Host和Accept-Encodin；result接收返回结果httpbin.org和gzip, deflate,即预期结果
    def test_2(self,headers,key,result):
        '''校验header里host的值'''
        Method = self.RequestMethod
        resp = base.get_response(self.url, Method)
        # connectHost = resp['headers']['host']
        connectHost = resp[headers][key]
        self.assertEqual(connectHost,result)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()