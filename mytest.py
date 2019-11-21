import unittest
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

class MyTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(8,add(5,4))

    def test_subtract(self):
        self.assertEqual(2,subtract(5,3))

if __name__=='__main__':
    unittest.main()



