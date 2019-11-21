# -*- coding: utf-8 -*-
__author__ = "FTest"
'''
下面来看一个函数，它接受名和姓并返回整洁的姓名：
'''
# def get_formatted_name(first_name,last_name):
#     '''返回整洁的姓名'''
#     full_name = first_name +' '+ last_name
#     return full_name.title()
#
# musician = get_formatted_name("Michael","Jordan")
#
# print(musician)
def get_formatted_name(first_name,last_name,middle_name=''):
    pass
    if middle_name:
        full_name = first_name + middle_name +last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jim','hanker')
print(musician)

musician2 = get_formatted_name('Li','min','shi')

print(musician2)



