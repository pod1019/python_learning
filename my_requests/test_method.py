import unittest

class TestMethod(unittest.TestCase):
    #类方法
    @classmethod
    def setUpClass(cls):
        print('类之前执行的方法：setUpClass(cls)','\r\n')
    @classmethod
    def tearDownClass(cls):
        print('类执行之后的方法：tearDownClass(cls)')


    #每次测试方法执行之前执行
    def setUp(self):
        print('test-->setup,每次测试方法执行之前执行')

    #每次测试方法执行之后执行
    def tearDown(self):
        print('test---->teardown,每次测试方法执行之后执行')

    #测试方法必须以test_开头
    def test_01(self):
        print('这是第一个测试方法！test01')

    def test_02(self):
        print('这是第二个测试方法！test02')
    def test_03(self):
        pass

if __name__ == '__main__':
    unittest.main()