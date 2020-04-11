# test_fixt.py
# coding:utf-8
import pytest
# 函数式

'''
setup_module/teardown_module
1.setup_module是所有用例开始前只执行一次，teardown_module是所有用例结束后只执行一次'''
def setup_mudule():
    print('setup_mudule: 整个.py模块只执行一次')
    print('比如： 所有用例开始前只打开一次浏览器')
# teardown_module是所有用例结束后只执行一次
def teardown_module():
    print('teardown_module: 整个.py模块只执行一次')
    print('比如：所有用例执行完后，只关闭浏览器')

# 每个用例开始前都会执行
def setup_function():
    print('setup_function: 每个用例开始前都会执行')

def teardown_function():
    print('teardown: 每个用例结束后都会执行')

def test_one():
    print('正在执行---test_one')
    x = 'this'
    assert 'b' in x

def test_two():
    print('正在执行---test_two')
    x = 'hello'
    assert hasattr(x,'check')

def test_three():
    print('正在执行---test_three')
    a = 'hello'
    b = 'hello world'
    assert a in b


if __name__ == '__main__':
    pytest.main(["-s","test_fixt.py"]) # 备注：-s参数是为了显示用例的打印信息。 -q参数只显示结果，不显示过程
    pytest.main(["-q","test_fixt.py"]) # 备注：-s参数是为了显示用例的打印信息。 -q参数只显示结果，不显示过程
