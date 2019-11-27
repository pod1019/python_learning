# -*- coding: utf-8 -*-
__author__ = "FTest"

#以下实例通过使用 if...elif...else 语句判断数字是正数、负数或零：


try:
    num = float(input("请输入一个数："))
    if num > 0:
        print("正数")
    elif num == 0:
        print("0")
    else:
        print("负数")
except ValueError:
    print("输入无效，请输入一个数字")