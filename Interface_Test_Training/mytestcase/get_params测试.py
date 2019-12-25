import requests
import json

host = 'https://httpbin.org/'
endpoint = 'get'
url = ''.join([host,endpoint])
params = {'show_env':1}

'''给服务器发送请求'''
r = requests.get(url=url,params=params)
print(r.text)


