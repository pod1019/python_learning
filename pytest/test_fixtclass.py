#test_fixtclass.py
# coding:utf-8
'''运行的优先级：setup_class》setup_method》setup 》用例》teardown》teardown_method》teardown_class
备注：这里setup_method和teardown_method的功能和setup/teardown功能是一样的，一般二者用其中一个即可
'''
import pytest
class TestCase():

    def setup(self):
        print("setup: 每个用例开始前执行")

    def teardown(self):
        print("teardown: 每个用例结束后执行")

    def setup_class(self):
        print("setup_class: 所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之后")

    def setup_method(self):
        print("setup_method:  每个用例开始前执行")

    def teardown_method(self):
        print("teardown_method:  每个用例结束后执行")

    def test_one(self):
        print("正在执行----test_one")
        x = "this"
        assert 'h' in x

    def test_two(self):
        print("正在执行----test_two")
        x = "hello"
        assert hasattr(x, 'check')

    def test_three(self):
        print("正在执行----test_three")
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == "__main__":
    pytest.main(["-s", "test_fixtclass.py"])