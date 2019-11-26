# 测试try...except...else结构
try:
    a = input("请输入被除数：")
    b = input("请输入除数：")
    c = float(a)/float(b)
except BaseException as e:
    print("有异常...",e)
else:
    print("两数相除的结果是：",c)