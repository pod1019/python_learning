result = len([x for x in list(range(100000)) if ('4') not in str(x)])
print(result)

d = 10
if d:
    print("d")

s = "False"
if s:
    print("非空字符串，是True")

s1 =""
if s1:
    print("非空字符串，是True")

#三元条件运算符
#print("s2是小于10的数" if int(s2)<10 else "s2不小于10")

score = int(input("请输入一个数字："))

if score<60:
    grade = "不及格"
elif score<80:
    grade = "及格"
elif score <90:
    grade = "良好"
else:
    grade = "优秀"

print("分数是{0}，等级是{1}".format(score,grade))




