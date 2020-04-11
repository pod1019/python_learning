from unittest import mock
import unittest
import temple

class Test_zhifu_status(unittest.TestCase):
    def test_01(self):
        temple.zhifu = mock.Mock(return_value={"result":"success","reason":"null"})
        status = temple.zhifu_status()
        print(status)
        self.assertEqual(status,"支付成功")

    def test_02(self):
        temple.zhifu = mock.Mock(return_value={"result": "fail", "reason":"余额不足"})
        status = temple.zhifu_status()
        print(status)
        self.assertEqual(status,"支付失败")

if __name__ == "__main__":
    unittest.main()