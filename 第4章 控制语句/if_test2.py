#选择结构
# 输入一个分数。分数在 0-100 之间。90 以上是 A,80 以上是 B，70 以上是 C，60
# 以上是 D。60 以下是 E。

score = int(input( " 请输入一个在0-100之间的数字："))
degree =  "ABCDE"
num = 0
if score>100 or score<0:
    score = int(input("输入错误！请重新输入一个在0-100之间的数字："))
else:
    num = score//10
    if num<6:
        num=5
print("分数是 {0}, 等级是 {1}".format(score,degree[9-num]))