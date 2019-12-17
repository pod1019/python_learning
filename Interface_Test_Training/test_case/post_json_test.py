import unittest
import requests
import json
from public import Config
from public import base

class PostJsonTest(unittest.TestCase):
    def setUp(self):
        host = Config.url()
        endpoint = 'get'
        self.url = base.get_url(endpoint)

    def test_post_json(self):
        data = {
            "info":{"code":1,"sex":'男',"id":1900,"name":"巧吧软件测试"},
            "code":1,
            "name":"巧吧软件测试",
            "sex":'女',
            "data":[{"code":1,"sex":'男',"id":1900,"name":"巧吧软件测试"},{"code":1,"sex":'女',"id":1900,"name":"巧吧软件测试"}],
            "id":1900
        }
        r = requests.post(self.url,json=data)
        resp = json.loads(r.text)
        name = resp.get('data')
        self.assertIsInstance(name,str)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()