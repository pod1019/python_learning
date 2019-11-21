# -*- coding: utf-8 -*-
__author__ = "FTest"

# course = open('e:\Demo\course.txt','w',encoding='utf8')
#
# course.write('机构：优品课堂\n')
#
# course.close()
#
names = ['tom','jerry','mike']
# f = open('e:\Demo\course.txt','w',encoding='utf8')
# a =0
# while a <10:
#     f.writelines(str(names+'\n')
#     a+=1

#想把这个list里的内容  写入到一个文件，写10次， 每一次写完 换行
with open('e:\Demo\course.txt', 'w', encoding='u8') as f:
    for x in range(10):
        f.writelines(','.join(names) + "\n")
