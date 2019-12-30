import unittest
from public import base

class PostJsonTest(unittest.TestCase):
    def setUp(self):
        endpoint = 'post'
        self.url = base.get_url(endpoint)

    def test_post_json(self):
        json = {
            "info":{"code":1,"sex":'男',"id":1900,"name":"巧吧软件测试"},
            "code":1,
            "name":"巧吧软件测试",
            "sex":'女',
            "data":[{"code":1,"sex":'男',"id":1900,"name":"巧吧软件测试"},{"code":1,"sex":'女',"id":1900,"name":"巧吧软件测试"}],
            "id":1900
        }
        # r = requests.post(self.url,data=json.dumps(data))
        DataALL = {'data':json}   #由于每个测试用例要传递的参数数量不一样，所以我们把参数封装成字典的形式
        Method = 'post'
        resp = base.get_response(self.url,Method,**DataALL) #**DataALL关键字参数

        name = resp.get('data')
        self.assertIsInstance(name,str)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
