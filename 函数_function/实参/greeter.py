# -*- coding: utf-8 -*-
__author__ = "FTest"
#
def greet_user():
    '''显示简单的问候语'''
    print("打印hello！")

greet_user()

def greet_user(username):
    '''显示简单的问候语'''
    print("Hello,"+username.title() +"!")

greet_user("jack")

def greet_user(username,age):
    '''显示简单的问候语及年龄'''
    print("Hello,"+username.title()+ "年龄是："+age.title())

greet_user("jerry","19")

str1 = "abcdefgh"
print(list(str1))
print(tuple(str1))

def favorite_book(name):
    print("One of my favorite boos is " + name.title())
favorite_book("Alice of wanderland")


