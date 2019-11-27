''''''
'''利用 for 循环，计算 1-100 之间数字的累加和；计算 1-100 之间偶数的累加和，计算 1-100 之间奇数的累加和'''

sum = 0
ou_sum = 0
ji_sum = 0

for i in range(1,101):
    sum += i
    if i % 2 == 0:
        ou_sum += i
    if i % 2 !=0:
        ji_sum += i

print(f'1~100之间数的累加和是：{sum},\r\n1~100之间的偶数累加和是：{ou_sum},\r\n1~100之间的偶数累加和是：{ji_sum}\r\n')