# -*- coding: utf-8 -*-
__author__ = "FTest"
import calendar
#判断是否是闰年
while True:#可以输入多次
    try:
        year = int(input("请输入一个数:"))
        if (year % 4) == 0 and (year % 100)!= 0 or (year % 100) == 0:
            print("{0}是闰年".format(year))
        else:
            print("{0}不是闰年".format(year))
    except ValueError:
        print("输入不合法，请输入整数")



#另一个方法判断闰年  Python 的 calendar 库中已经封装好了一个方法 isleap() 来实现这个判断是否为闰年：
print(calendar.isleap(int(input("请输入一个数字1111111111啊啊："))))

