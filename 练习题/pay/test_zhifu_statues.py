from unittest import mock
import unittest
import temple

class Test_zhifu_status(unittest.TestCase):
    '''单元测试用例'''
    def test_01(self):
        '''测试支付成功场景'''
        # mock 一个支付成功的数据
        temple.zhifu = mock.Mock(return_value={"result":"success","reason":"null"})

        # 根据支付结果测试页面跳转
        statues = temple.zhifu_statues()
        print(statues)
        self.assertEqual(statues,"支付成功")


    def test_02(self):
        '''测试支付失败场景'''
        #mock 一个支付失败的数据
        temple.zhifu = mock.Mock(return_value={"result":"fail","reason":"余额不足"})
        # 根据支付结果测试页面跳转
        statues = temple.zhifu_statues()
        self.assertEqual(statues,"支付失败")
if __name__ == "__main__":
    unittest.main()
