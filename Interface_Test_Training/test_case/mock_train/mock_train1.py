import unittest
from unittest import mock
from .modular import Count

class TestCount(unittest.TestCase):

    def test_add(self):
        count = Count()
        count.add = mock.Mock(name='add',eturn_value=7)
        # count.add = mock.Mock(return_value=count.add2(2,3))
        # return_value= 和 side_effect都存在时，return_value失效。
        count.add = mock.Mock(return_value=7,side_effect=count.add2)
        # print(count.add)
        result = count.add(8,5) #实际传入的参数
        count.add.assert_called_with(8,5) #断言传入的参数；检查传递的参数是否正确
        count.add.assert_called_once_with(8,5)
        count.add(2,4)
        # count.add.assert_called_once_with(2,4)
        count.add.assert_any_call(2,4)
        print(result)
        self.assertEqual(result,13)

if __name__=='__main__':
    unittest.main()