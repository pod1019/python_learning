# 打印九九乘法表
for m in range(1, 10):
    for n in range(1, m+1):
        print("{0}*{1}={2}".format(n,m,(n*m)),end="\t")
    print()
# 生成列表推导式
li = [x for x in range(1,6)]
print(li)
li2 = [x*2 for x in range(10)]
print(li2)

# 绘制多个同心圆
import turtle

t = turtle.Pen()
my_color = ("red","green","yellow","black")

t.width(4)
t.speed(1)

for i in range(10):
    t.penup()
    t.goto(0, -i*10)
    t.pendown()
    t.color(my_color[i % len(my_color)])
    t.circle(15+i*10)

turtle.done(); # 程序执行完，窗口仍然在




