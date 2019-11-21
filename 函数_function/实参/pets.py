# -*- coding: utf-8 -*-
__author__ = "FTest"

#传递实参 位置实参

def discribe_pet(animal_typy,pet_name):
    """显示宠物的信息"""
    print("\nI hava a " +animal_typy+".")
    print("My " + animal_typy + "'s name is " + pet_name.title()+".")

discribe_pet('dog','小黑')
discribe_pet('cat','mimi')
print("-------------分割--------------")

#关键字实参
def discribe_pet2(animal_type,pet_name):
    """显示宠物的信息"""
    print("I hava a " + animal_type + ".")
    print("My " + animal_type + "'s name is " +pet_name.title()+".")

discribe_pet2(animal_type='Dog',pet_name='Trump')
print("-------------分割--------------")

#默认值参数，只传形参中没有给定具体值的参数 pet_name
def discribe_pet3(pet_name,animal_type="Pig"):
    print("I hava a " + animal_type)
    print("My " + animal_type + "'s name is "+ pet_name +".")
discribe_pet3(pet_name="安倍")


