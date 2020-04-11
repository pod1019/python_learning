import unittest
from unittest import mock
from .modular import Count
'''关键字参数return_value, side_effect'''
class TestCount(unittest.TestCase):

    def test_add(self):
        count = Count()
        ''':return_value的三种方式'''
        # 1、直接返回一个具体值
        # count.add = mock.Mock(return_value=7)
        # 2、通过调用函数add后，函数计算出结果后再返回
        # count.add = mock.Mock(return_value=count.add(2,3))
        # 3、用side_effect替换;【return_value=7,side_effect两个都存在时，return_value不起作用】
        count.add = mock.Mock(return_value=7,side_effect=count.add2) # 是函数替换，注意理解
        print('-----',count.add)
        result = count.add(5,8)  # 由于上面mock.Mock设置了returen_value=7作为返回值，所以result的值就没有从conunt.add(8,5)取【如果取，是13，而不是7了】
        print('result的结果是：',result)
        self.assertEqual(result,13)


if __name__=='__main__':
    unittest.main()