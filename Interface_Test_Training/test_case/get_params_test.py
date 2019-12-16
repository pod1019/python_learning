import requests
import json
import unittest

class GetParams(unittest.TestCase):
    '''GetParams测试'''  # 前面的注释是后面执行测试用例后，产生的测试报告里的概要信息
    def setUp(self):
        host = 'http://httpbin.org/'
        endpoint = 'get'
        self.url = ''.join([host,endpoint])

    def test_get_params1(self):
        '''test_get_params1测试连接的主机'''# 前面的注释是后面执行测试用例后，产生的测试报告里的概要信息
        params = {'show_env':1}
        '''给服务器发送请求'''
        r = requests.get(self.url,params=params)
        resp = r.json()
        connecthost = resp.get('headers').get('Host')
        self.assertEqual(connecthost,"httpbin.org")

    def test_get_params2(self):
        params = {'show_env':1}
        '''给服务器发送请求'''
        r = requests.get(self.url,params=params)
        resp = r.json()
        connecthost = resp.get('headers').get('Host')
        self.assertIsInstance(connecthost,str) # 判断取得的结果的类型是不是str类型

    def tearDown(self):
        pass

if  __name__ == '__main__':
    unittest.main()