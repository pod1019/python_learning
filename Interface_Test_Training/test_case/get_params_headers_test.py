import requests
import unittest

class GetParamsHeadersTest(unittest.TestCase):
    '''Get有params和headers测试'''
    def setUp(self):
        host = 'http://httpbin.org'
        endpoint = 'get'
        self.url = ''.join([host,endpoint])

    def test_params_headers(self):
        '''验证浏览器是否chrome'''
        params = {'show_env':1}
        headers= {
            'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36',
            'Accept-Encoding':'gzip, deflate',
            'Accept':'*.*',
            'Connection':'keep-alive'}
        '''给服务器发送请求'''
        r = requests.get(self.url,params=params,headers=headers,stream=True)
        resp = r.json()
        User_Agent = resp['headers']['User-Agent']
        self.assertEqual('Chrome',User_Agent)
    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()

