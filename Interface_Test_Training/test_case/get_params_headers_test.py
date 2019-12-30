import unittest
from public import base

testcasefile = 'get_params_headers_test_data.xlsx'
AllData = base.get_data(testcasefile,'AllData') # 获取测试用例文件 testcasefile，并进一步取到该文件的sheet名，即AllData
TestData = base.get_data(testcasefile,'TestData') # 获取测试用例文件 testcasefile，并进一步取到该文件的sheet名，即TestData
# 怎么获得endpoint信息呢？
#先打印一下AllData 和 TestData，看看这两个的内容，然后再从它俩内容中获取endpoint信息
print(AllData)
print(TestData)
# 1、取endpoint
EndPoint = AllData[1][1] # 取到endpiont信息，并赋值给Endpoint
# 2、取Method
RequestMethod = AllData[1][2]
# 3、取DataAll
DataAll = TestData[1][1]  #DataAll是从TestData这个sheet里面取的。
# 4、取预期结果 从TestData这个sheet里取
expectedresult = TestData[1][2]

class GetParamsHeadersTest(unittest.TestCase):
    '''Get有params和headers测试'''
    def setUp(self):
        # endpoint = 'get' 由于本文件上面 已经把endpoint已经取到，所以endpoint = EndPoint即可，不用再直接把‘get’赋给endpoint
        endpoint = EndPoint
        self.url = base.get_url(endpoint)

    def test_params_headers(self):
        '''验证浏览器是否chrome'''
        # params = {'show_env':1}
        # headers= {
        #     'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36',
        #     'Accept-Encoding':'gzip, deflate',
        #     'Accept':'*.*',
        #     'Connection':'keep-alive'
        # }
        '''给服务器发送请求'''
        # resp1 = requests.get(self.url,params=params,headers=headers,stream=True)
        # DataALL = {'params':params,'headers':headers}   #由于每个测试用例要传递的参数数量不一样，所以我们把参数封装成字典的形式
        DataALL = eval(DataAll) # 由于从excel文件里取到的 DataAll 是字符串，但本语句左边的大写的 DataALL 是可变参数（是字典），所以通过eval()把DataAll转换一下
        # Method = 'get' #由于本文件上面 已经把Method已经取到，所以Method = RequestMethod即可，不用再直接把‘get’直接赋给Method
        Method = RequestMethod
        resp = base.get_response(self.url, Method, **DataALL)  # **DataALL关键字参数

        User_Agent = resp['headers']['User-Agent']  #取一个实际结果保存为User_Agent，然后下面用断言进行比较
        # self.assertIn('Mozilla',User_Agent) # Mozilla预期结果，User_Agent实际结果
        # 上面已经取到预期结果 expectedresult ，self.assertIn('Mozilla',User_Agent)，可以替换成下面的语句
        self.assertIn(expectedresult, User_Agent)
        print(expectedresult)
    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()

