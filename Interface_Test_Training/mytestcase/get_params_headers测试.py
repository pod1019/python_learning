import requests
import json
host = 'https://httpbin.org/'
endpoint = 'get'
url = ''.join([host,endpoint])

params = {'show_env':1}
headers = {"hahaha":"111222","Connection":"close","Content-Encoding":"gzip","User-Agent":"python-requests/2.22.0"}

'''给服务器发送请求'''
r = requests.get(url=url,params=params,headers=headers)

print(r.text)

