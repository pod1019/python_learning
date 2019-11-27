#选择结构
# 输入一个分数。分数在 0-100 之间。90 以上是 A,80 以上是 B，70 以上是 C，60
# 以上是 D。60 以下是 E。
score = int(input("请输入一个1到100之间的数字:"))
grade=""
if score>100 or score<0:
    score = int(input("输入不合法！请输入1到100之间的数字："))
else:
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=60:
        grade="D"
    else:
        grade="E"
    print("分数是：{0},等级是：{1}".format(score,grade))