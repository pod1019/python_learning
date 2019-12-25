'''会话对象 session 是客户端与服务器之间的会话，用来保存用户的信息'''
import requests

host = 'http://httpbin.org'
endpoint = 'cookies/set/sessioncookie/123456789'
url = ''.join([host,endpoint])
url1 = 'http://httpbin.org/cookies'

'''1、保持会话步骤'''
# 发送请求
r = requests.get(url1) #这个方法无法获取到cookies，因为url1里没有具体的cookies值
print(r.text)

# 怎么能让访问url1 还能得到cookies呢

session = requests.session() # 初始化一个session对象，起到保持会话的作用
session.get(url) # 把cookies信息存在了session中
r1 = session.get(url1) #通过会话获取url地址
print('r1----',r1.text)
'''2、通过session保存一些会话信息,比如下面例子把header信息保存到服务器'''
header1 = {'test1':'aa'}
header2 = {'test2':'bb'}
session1 = requests.session()
session1.headers.update(header1) # 已经存到了服务器中的信息header1
r2 = session1.get('http://httpbin.org/headers',headers=header2) # 发送新的headers信息，即header2
print(r2.text)

'''3、删除已存在的会话信息，设置为None'''
session1.headers['test1'] = None  # 删除会话信息，只需要赋值None即可。就把session1的header1给删掉了
r3 = session1.get('http://httpbin.org/headers',headers=header2)
print(r3.text)