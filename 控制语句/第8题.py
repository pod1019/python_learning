salarySum=0  # 总薪资

empNums=0 # 已录入的员工个数
salarys=[]

while True:

    s = input('请输入员工的薪资（按Q或q结束）：')  # 工资

    if s.upper() == 'Q':
        print('录入完成，退出')
        break
    if float(s)<0:
        continue
    empNums+=1
    salarys.append(float(s)) # 把工资追加到列表中
    print(salarys)
    salarySum+=int(s) # 工资累加



