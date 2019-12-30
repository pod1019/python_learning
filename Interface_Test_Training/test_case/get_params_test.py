import unittest
from public import base

class GetParams(unittest.TestCase):
    '''GetParams测试''' # 产生的测试报告里的概要信息，就是此注释的内容
    def setUp(self):
        endpoint = 'get'
        self.url = base.get_url(endpoint)

    def test_get_params1(self):
        '''test_get_params1测试连接的主机'''# 产生的测试报告里的概要信息，就是此注释的内容
        params = {'show_env':1}
        '''给服务器发送请求'''
        # resp = HttpService.MyHTTP().get(self.url,params)
        DataALL = {'params':params} #由于每个测试用例要传递的参数数量不一样，所以我们把参数封装成字典的形式
        Method = 'get'
        resp = base.get_response(self.url,Method,**DataALL)

        connecthost = resp.get('headers').get('Host')
        self.assertEqual(connecthost,"httpbin.org")

    def test_get_params2(self):
        '''test_get_params测试'''
        params = {'show_env':1}
        '''给服务器发送请求'''
        DataALL = {'params':params} #由于每个测试用例要传递的参数数量不一样，所以我们把参数封装成字典的形式

        Method = 'get'
        resp = base.get_response(self.url, Method, **DataALL)

        connecthost = resp.get('headers').get('Host')
        self.assertIsInstance(connecthost,str) # 判断取得的结果的类型是不是str类型

    def tearDown(self):
        pass

if  __name__ == '__main__':
    unittest.main()
