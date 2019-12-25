import requests
import json
host = 'https://httpbin.org/'
endpoint = 'post'
url = ''.join([host,endpoint])

params = {'show_env':1}
data = {'a':'软件测试','b':'form-data11'}

r = requests.post(url,params=params,data=data)
print(r.text) #取出来后，data的数据中文字符会以unicode编码形式的。
# 下面用另一种方式直接显示出来中文字符 借助json模块
resp = r.json()
print(resp['form'])