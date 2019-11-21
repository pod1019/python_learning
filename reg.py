import datetime
# 注册
# 1、已经存在的用户不让注册了，提示用户已存在
# 2、两次输入的密码一致才可以注册成功
user_list = ['user1']
passwd_list = ['123']

# for i in range(3):
#     username = input('username:')
#     passwd = input('passwd:')
#     cpasswd = input('cpasswd:')
#     if user_list.count(username) > 0:
#         print('用户名已存在！')
#     elif passwd != cpasswd:
#         print('两次输入的密码不一致！')
#     else:
#         user_list.append(username)
#         passwd_list.append(passwd)
#         print('注册成功！')
#
#         print(user_list)
#         print(passwd_list)

# -----------------------------------------------------------
# 登录
# 1、如果用户不存在要给出提示
# 2、最多3次机会
# 3、要校验为空

# 1、循环3次，输入账号和密码
# 2、判断用户是否存在
# 3、找到username的下标，然后拿着下表去passwd_list里找密码
# 4、判断输入的密码是否与passwd_list里的密码一致

for i in range(3):
    username = input('username:')
    password = input('password:')
    if username not in user_list:
        print('用户名不存在！')
    elif username == '':
        print('用户名不能为空')
    else:
        index = user_list.index(username)
        p = passwd_list[index]
        if password == p:
            print('登录成功！%s'% datetime.datetime.today())
        else:
            print('密码错误！')


