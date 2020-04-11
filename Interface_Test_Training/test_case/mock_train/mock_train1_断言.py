import unittest
from unittest import mock
from .modular import Count
from .modular import *

class TestCount(unittest.TestCase):

    def test_add(self):
        count = Count()
        count.add = mock.Mock(name='add',eturn_value=7)
        # count.add = mock.Mock(return_value=count.add2(2,3))
        # return_value= 和 side_effect都存在时，return_value失效。
        count.add = mock.Mock(return_value=7,side_effect=count.add2)
        # print(count.add)
        result = count.add(8,5) #实际传入的参数

        # 断言传入的参数；检查传递的参数是否正确 如果传入错误参数(1,5)则报： AssertionError: Expected call: mock(1, 5) Actual call: mock(8, 5)
        count.add.assert_called_with(8,5)

        # count.add.assert_called_once_with(8,5)
        count.add(2,3)
        # count.add.assert_called_once_with(2,3)
        count.add.assert_any_call(2,3)

        print('已使用的参数：',count.add.call_args)
        print('已使用的参数列表：',count.add.call_args_list)

        param1 = mock.call(8,5)
        param2 = mock.call(2,3)
        count.add.assert_has_calls([param1,param2],any_order = False)
        count.add.assert_has_calls([param2,param1],any_order = True)

        print('count.add是否被调用：',count.add.called)
        print('count.add的调用次数：',count.add.call_count)
        print(count.add.call_args)
        print(count.add.call_args_list) # 只有参数调用（工厂）
        print(count.add.method_calls) # 只有方法调用
        print(count.add.mock_calls) # 包含参数传递（工厂）和方法传递

        mockFoo = mock.Mock(spec=Count)
        mockFoo.add(1,1)
        mockFoo.add(1,2)

        print(mockFoo.method_calls) # 只有方法调用
        print(mockFoo.mock_calls) # 包含参数传递（工厂）和方法传递

        print('实际结果result的值是：',result)
        self.assertEqual(result,13)

if __name__=='__main__':
    unittest.main()