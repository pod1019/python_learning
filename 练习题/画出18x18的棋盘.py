# 画出18*18的棋盘
import turtle
t = turtle.Pen()
n = 30; #两条线间隔

x = -300 #x初始值
y = -300 #y初始值
t.penup()
for i in range(5):

    t.goto(-300,400+ y + -i*n)
    t.pendown()
    t.forward(5 * n)
    t.penup()

for i in range(5):
    t.goto(400 + x + -i*n ,-300)
    t.pendown()
    t.forward(5 * n)
    t.penup()

turtle.done()
