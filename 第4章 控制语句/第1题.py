''''''
'''
#1、输入一个学生的成绩，将其转化成简单描述：不及格(小于 60)、及格(60-79)、良好 (80-89)、优秀(90-100)
'''

raw_input = input("请输入分数:")  # 这里输入的是字符串类型
score = int(raw_input) # 将输入的字符串转化为int型
grade = ''
if score < 60:
    grade = "不及格"
if score < 80:
    grade = "及格"
if score < 90:
    grade = "良好"
if score <= 100:
    grade = "优秀"

# print("分数是:{0},等级是:{1}".format(score, grade))
# print(f"分数是:{score}",f"等级是:{grade}")
print(f"分数是：{score},等级是：{grade}")

