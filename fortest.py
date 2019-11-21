# -*- coding: utf-8 -*-
__author__ = "FTest"

sum_all=0
sum_jishu = 0
sum_oushu = 0
for num in range(101):
    sum_all += num
    if num%2==0:
        sum_oushu += num
    else:
        sum_jishu +=num

print("1-100的累加和是{0},奇数和是{1},偶数和是{2}".format(sum_all,sum_jishu,sum_oushu))