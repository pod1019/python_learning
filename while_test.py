#while练习
#利用 while 循环打印从 0-10 的数字。
num = 0
while num<10:
    if num<9:
        print(num,end='、')
        num += 1
    else:
        print(num)
        num += 1

# 【操作】利用 while 循环，计算 1-100 之间数字的累加和；计算 1-100 之间偶数的累加和，
# 计算 1-100 之间奇数的累加和。