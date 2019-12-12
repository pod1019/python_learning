# coding=utf-8
import unittest
from my_requests.RunMain1 import RunMain


class TestRun1(unittest.TestCase):
    def setUp(self):
        self.run_main1 = RunMain()
        print('test---->setUp,每次测试方法执行之前执行')

    def tearDown(self):
        self.run_main1 = RunMain()
        print('test---->teardown,每次测试方法执行之后执行')
# 测试用例必须以test开头

    def test_01(self):
        url = 'http://118.25.179.224:3000/login/cellphone'
        data = {
            'phone':'18916051977',
            'password':'654321'
        }
        print('执行测试方法test_01')
        # url1 = 'http://httpbin.org/post'
        # data1 = {
        #     'key1':'value1',
        #     'key2':'value2',
        # }

        res = self.run_main1.run_main('get',url,data)

if __name__=='__main__':
    # 实例化TestSuite创建测试套件
    suite = unittest.TestSuite

    # 把用例test_01添加到测试套件中
    suite.addTest(TestRun1('test_01'))