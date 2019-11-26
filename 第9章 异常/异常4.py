# 多个except结构
try:
    a = input("请输入被除数:")
    b = input("请输入除数:")
    c = float(a)/float(b)
    print("两数相除的结果是：",c)
except ZeroDivisionError:
    print("异常：除数不能为0")
except TypeError:
    print("异常：除数和被除数都应该为数值类型")
except NameError:
    print("异常：变量不存在")
except BaseException as e:
    print(e)
    print(type(e))

finally: # 无论如果，此语句必然执行
    print("kkkkkkkkk")