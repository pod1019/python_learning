
import requests
import json
#1、导入unittest模块
import unittest
# 2、定义测试类、父类是unittest.TestCase
class GetParams(unittest.TestCase):
    '''3、定义setUp()
        # 该方法用于测试用例执行前的初始化工作。
        # 注意，所有类中方法的入参为self，定义方法的变量也要“self.变量”
        # 注意，输入的值为字符型的需要转为int型
    '''
    def setUp(self):
        host = 'https://httpbin.org/'
        endpoint = 'get'
        self.url = ''.join([host,endpoint])
# 4、定义测试用例，以“test_”开头命名的方法。方法的入参是self，可使用unittest.TestCase类下面的各种断言方法用于对测试结果的判断
    def test_get_params1(self):
        params = {'show_env':1}
        '''给服务器发送请求'''
        r = requests.get(self.url,params=params)
        # print(r.text)
        resp = r.json()
        connect = resp.get('headers').get('Host')
        self.assertEqual(connect,'httpbin.org') # 断言 检查结果是不是等于 httpbin.com

    @unittest.skip(reason='sss')
    def test_get_params2(self):
        params = {'show_env': 1}
        '''给服务器发送请求'''
        r = requests.get(self.url, params=params)
        resp = r.json()
        connect = resp.get('headers').get('Host')
        self.assertIn(connect,'myhoststr') #断言  判断结果是否在'myhoststr'中；
        self.assertIs(connect,33)

    @unittest.skipIf(5,reason='sss')
    def test_get_params3(self):
        params = {'show_env': 1}
        '''给服务器发送请求'''
        r = requests.get(self.url, params=params)
        resp = r.json()
        connect = resp.get('headers').get('Host')
        self.assertIn(connect, 'myhoststr')  # 断言  判断结果是否在'myhoststr'中；
        self.assertIs(connect, 33)

    def test_get_params4(self):
        params = {'show_env': 1}
        '''给服务器发送请求'''
        r = requests.get(self.url, params=params)
        resp = r.json()
        connect = resp.get('headers').get('Host')
        self.assertIsInstance(connect, str)  # 断言  检查结果是不是字符串

# 5、定义tearDown()方法用于测试用例执行之后的善后工作
    def tearDown(self):
        print('test over!')
# 6、执行测试
if __name__ =="__main__":
    unittest.main()