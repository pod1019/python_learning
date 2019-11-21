# -*- coding: utf-8 -*-
__author__ = "FTest"
'''
8-3 T 恤 ：编写一个名为 make_shirt() 的函数，它接受一个尺码以及要印到 T 恤上的字样。
这个函数应打印一个句子，概要地说明 T 恤的尺码和字样。
使用位置实参调用这个函数来制作一件 T 恤；再使用关键字实参来调用这个函数
'''

def make_shirt(size,LOGO):
    print("这个T恤的尺码是：" + size + "\r\n" + "T恤上的字样是：" + LOGO)
print("我是位置实参："+"\r")
make_shirt("L号","666,Made in china!")

print("----------------------")

print("我是关键字实参："+"\r")
make_shirt(size="L号",LOGO="666,Made in china!")



