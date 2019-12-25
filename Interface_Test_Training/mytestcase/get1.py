import requests
import json
# host = 'https://postman-echo.com/'
# endpoint = 'get'
# url = ''.join([host,endpoint])
url = 'http://www.aimilicai.com'
'''给服务器发送请求'''
r = requests.get(url)
# print(r.url) #获取URL
# print(r.status_code) #获取响应状态码

#下面两个方式 展现形式不一样。可以通过查看类型，是不一样的
# print(r.text) #unicode 文本
# print(type(r.text)) #查看r.text的类型 <class 'str'>
# print(r.content) #bytes 图片、文件等
# print(type(r.content)) #查看r.content类型 <class 'bytes'>

print('我是响应头:',r.headers) #响应头
print('我是请求头:',r.request.headers) #这个是请求头（是响应中把request属性的一些信息被带过来，比如请求头）
# 获取请求头的其他信息，比如url、method  不常用，用于调试
print(r.request.url)
print(r.request.method)

# response = r.json() # 把请求响应的对象 r 变成json串 ---常用