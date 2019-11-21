import datetime

while True:
    txt = input('请输入一个数字:')
    if txt == 'stop':
        break
    elif not txt.isdigit():
        print('你输入的不是数字！')
    else:
        num = int(txt)
        if num > 20:
            print('你输入的数字太大了！')
        elif num < 20:
            print('你输入的数字太小了！')
        else:
            print('恭喜你，猜对了！')
