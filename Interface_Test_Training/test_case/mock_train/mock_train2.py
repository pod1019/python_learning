import sys
import unittest
from unittest import mock
sys.path.append(',/mock_train')
import modular
# from test_case.mock_train import modular

'''一、mock一个函数'''
class TestCount1(unittest.TestCase):

    @mock.patch('modular.add_def') #1
    def test_add(self,mock_add_def): #2 加mock_add_def作为参数
        mock_add_def.return_value = 1 #3
        result = modular.add_def(8,5)
        print('---',result)
        self.assertEqual(result,13)
        mock_add_def.side_effect = modular.add_def2

'''二、mock对象里的一个方法'''
class TestCount2(unittest.TestCase):

    @mock.patch.object(modular.Count,'add') # 1mock.patch.object,带object的才是对应类的；注意和上面的patch的区别
    def test_add(self,mock_add): #2 加 mock_add作为参数
        count = modular.Count()
        mock_add.return_value = 2 #3
        mock_add.side_effect = modular.add_def2
        result = count.add(8,5)
        print(result)
        self.assertEqual(result,13)

'''三、mock多个函数(类（中的方法）、函数)，注意顺序'''
class TestCount3(unittest.TestCase):
    # 就近原则    modular.Count对应mock_add;   modular.add_def对应mock_add_def
    @mock.patch.object(modular.Count,'add') # 1mock.patch.object,带object的才是对应类的；注意和上面的patch的区别
    @mock.patch('modular.add_def')
    def test_add(self,mock_add_def,mock_add): # 注意：此处参数的顺序 和 装饰器的顺序正好相反！！！
        count = modular.Count()
        mock_add_def.return_value = 1
        mock_add.return_value = 13
        result1 = count.add(8,5)
        result2 = modular.add_def(8,5)
        print(result1,result2)
        self.assertEqual(result1,13)
        self.assertEqual(result2,13)

if __name__ == "__main__":
    unittest.main()

