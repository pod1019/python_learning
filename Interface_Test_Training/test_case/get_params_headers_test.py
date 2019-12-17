import unittest
from public import Config
from public import base
from public import HttpService

class GetParamsHeadersTest(unittest.TestCase):
    '''Get有params和headers测试'''
    def setUp(self):
        host = Config.url()
        endpoint = 'get'
        self.url = base.get_url(endpoint)

    def test_params_headers(self):
        '''验证浏览器是否chrome'''
        params = {'show_env':1}
        headers= {
            'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36',
            'Accept-Encoding':'gzip, deflate',
            'Accept':'*.*',
            'Connection':'keep-alive'
        }
        '''给服务器发送请求'''
        # resp1 = requests.get(self.url,params=params,headers=headers,stream=True)
        DataAll = {'params':params,'headers':headers}   #由于每个测试用例要传递的参数数量不一样，所以我们把参数封装成字典的形式
        resp = HttpService.MyHTTP().get(self.url,**DataAll)

        User_Agent = resp['headers']['User-Agent']
        self.assertIn('Mozilla',User_Agent)

    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()

