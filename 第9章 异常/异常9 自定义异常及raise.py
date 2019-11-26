#coding=utf-8
#测试自定义异常类
class AgeError(Exception): #继承Exception
    def __init__(self,errorInfo):
        Exception.__init__(self)
        self.errorInfo = errorInfo
    def __str__(self):
        # 用str包住self.errorInfo,是因为数值和字符串没法用+连接
        return "你输入的年龄是："+str(self.errorInfo) + ",年龄错误！应该在1-150之间"


###########测试代码#############
if __name__ == "__main__": ##如果为 True，则模块是作为独立文件运行，可以执行测试代码
    age = int(input("请输入一个年龄： "))
    if age<1 or age>=150:
        raise AgeError(age)
    else:
        print("正常的年龄： ",age)