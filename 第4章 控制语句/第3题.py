''''''
'''输入一个分数。分数在 0-100 之间。90 以上是 A,80 以上是 B，70 以上是 C，60 以上 是 D。60 以下是 E'''
import random
score = int(input('输入一个分数：'))
lever =''
if score>=90:
    lever='A'
if score>=80:
    lever='B'
if score>=70:
    lever='C'
if score>=60:
    lever='D'
if score<60:
    lever='E'
print(f"分数是：{score}, 等级是：{lever}")