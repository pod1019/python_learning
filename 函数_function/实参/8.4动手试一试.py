# -*- coding: utf-8 -*-
__author__ = "FTest"

'''
8-4  大号 T 恤 ：修改函数 make_shirt() ，使其在默认情况下制作一件印有字样 “I love Python” 的大号 T 恤。
调用这个函数来制作如下 T 恤：
一件印有默认字样的大号 T恤、一件印有默认字样的中号 T 恤和一件印有其他字样的 T 恤（尺码无关紧要）。
'''
def make_shirt(size,logo="I love Python"):
    print("这个T恤的尺寸是：" + size +","+ " 印的字样是：" +logo)
print("一件印有默认字样的大号 T恤:")
make_shirt("大号T恤")

print("-------------------------------")
print("一件印有默认字样的中号 T 恤:")
make_shirt("中号T恤")

print("-------------------------------")

make_shirt(size="xxL",logo="made in china")