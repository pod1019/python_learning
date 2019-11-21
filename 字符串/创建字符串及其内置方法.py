'''
字符串的本质是：字符序列。Python 的字符串是不可变的，我们无法对原字符串做任
何修改。但，可以将字符串的一部分复制到新创建的字符串，达到“看起来修改”的效果
'''
#1、创建字符串
msg = 'hello,welcome to Beijing'
s = ''  #创建一个空字符串
print(len(msg))
print(msg.capitalize()) # 将字符串的第一个字母变成大写,其他字母变小写
print(msg.endswith('g')) # 判断是否以g结尾
print('aa'.isidentifier()) # 判断字符串是否是有效的 Python 标识符，可用来判断变量名是否合法。
print('test'.center(20,'-')) # 20个'-',把test放在20个-中间的位置
print(msg.expandtabs(100))
print(msg.find('e')) # 查找字符串的索引
print('aBcd'.isalpha()) # 判断是否是英文字母
print('111'.isdigit()) # 判断是否是数字
print('aa'.islower())  # 是否是小写字母
print('AA'.isupper())  # 是否是大写字母
print('Chaguan'.istitle())  # 是不是一个标题，判断首字母是否大写
print('+'.join(['nihao', 'wohao', 'dajiahao']))  # 拼接字符串
print('AI ABCD'.lower())  # 变成小写
print('abcdef'.upper())  # 变成大写
print('-' * 20)

# 去空格和换行
print('\nmysql \n'.lstrip())  # 默认去掉左边的空格和换行
print('\nmysql \n'.rstrip())  # 默认去掉右边的空格和换行
print('\nmysql \n'.strip())  # 默认去掉两边边的空格和换行

# 字符串映射
s2 = str.maketrans('abcdefg', '1234567')  # 前面的字符串和后面的字符串做映射
print('af dd ff'.translate(s2))  # 输出按照上面maketrans做映射后的字符串

s3 = str.maketrans('1234567','abcdefg')
print('11 23 44'.translate(s3))

s4 = 'this is an apple'
print(s4.replace('this','that'))  # 替换字符串

print('1-2-3-4-5'.split('-')) # 以'-' 分割字符串，并返回一个列表 list

print('abc\n+ben-z\ndef'.splitlines()) # 按照换行符分割

print('abcDefineHello'.swapcase()) # 大小写反正，大变小，小变大
