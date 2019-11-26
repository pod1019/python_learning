#coding=utf-8
# 得失trackback模块的使用
import traceback
try:
    print("step1")
    num = 1/0
except:
    with open("aa.txt","a",encoding="utf-8") as f:
        traceback.print_exc(file=f)
