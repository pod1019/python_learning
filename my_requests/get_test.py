import requests
import json

'''给服务器发送请求'''
host = 'https://httpbin.org/'
endpoint = 'get'
url = ''.join([host,endpoint])
r = requests.get(url)

# print(url) 获取url
# print(r.status_code,r.reason) #获取响应状态码，获取状态码的原因

response = r.json()
print(response['headers'])

print(response['headers']['Accept-Encoding'])

# response 和 eval(r.text) 是一样效果的
print(type(response))
print(type(eval(r.text)))



print(eval(r.text)['headers']['Accept-Encoding'])

