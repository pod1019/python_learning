#coding=utf-8
#
# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行
#
# 2.注释：包括记录创建时间，创建人，项目名称。
#
# 3.导入unittest模块
#
# 4.定义测试类，父类为unittest.TestCase。
#
# 5.定义setUp()方法用于测试用例执行前的初始化工作。(设置测试包参数)
#
# 6.定义测试用例，以“test_”开头命名的方法(使用unittest.TestCase类下的断
#
# 言对用例是否测试通过进行判断,也可以使用@unittest.skip来跳过测试用例)
#
# 7.定义tearDown()方法用于测试用例执行之后的善后工作。
#
# 执行测试用例,并输出测试结果