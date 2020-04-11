import unittest
from unittest import mock
from .modular import Count

class TestCount(unittest.TestCase):

    def test_add(self):
        count = Count()
        count.add = mock.Mock(name='add3333')
        print('-----',count.add)
        result = count.add(5,8)
        print(result)
        self.assertEqual(result,13)

if __name__=='__main__':
    unittest.main()