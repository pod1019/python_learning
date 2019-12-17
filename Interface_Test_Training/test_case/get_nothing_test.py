import unittest
import requests
import json

class GetNothingTest(unittest.TestCase):
    '''GET无参数测试'''
    def setUp(self):
        host = 'http://httpbin.org/'
        endpoint = 'get'
        self.url = ''.join([host,endpoint])

    def test_1(self):
        '''校验状态码是否为200'''
        r = requests.get(self.url)

        status_code = r.status_code
        self.assertEqual(status_code,200)

    def test_2(self):
        '''校验header李connection的值'''
        r = requests.get(self.url)
        resp = r.json()
        print(resp)
        connectHost = resp['headers']['Host']
        self.assertEqual(connectHost,'httpbin.org')
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()