import requests
import json
from public import Config
from public import base

# 第一步导入unittest等模块
import unittest
# 第2步：定义测试类必须继承unittest.TestCase类
class PostDataTest(unittest.TestCase):
    '''Post Data测试'''
#     主要是环境配置:进行测试前的初始化工作,比如在接口测试前面的一些前置的参数赋值,数据库操作等4
    def setUp(self):
        host = Config.url()
        endpoint = 'get'
        self.url = base.get_url(endpoint)

#     第4步：定义测试用例，名字必须以"test"开头
    def test_post_data_1(self):
        '''form值验证'''
        params = {'fan':1}
        data = {'a':'巧吧软件测试','b':'form-data'}


        r = requests.post(self.url,params=params,data=data)
        resp = r.json()
        form = resp.get('form').get('a')

        # 第5步：定义assert断言，判断测试结果
        self.assertEqual(form,'巧吧软件测试')

        @unittest.skip('无条件跳过')
        def test_post_data_2(self):
            '''form值type类型判断'''

        def tearDown(self):
            pass

if __name__ == "__main__":
    unittest.main()