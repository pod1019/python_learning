import requests
import json
host = 'https://httpbin.org/'
endpoint = 'post'
url = ''.join([host,endpoint])

data = {
    "info":{"code":1,"sex":"男","id":1900,"name":"软件测试"},
    "code":1,
    "name":"软件测试",
    "sex":"女",
    "data_1":[
        {"code":1,"sex":"男","id":1901,"name":"软件测试1"},
        {"code":2,"sex":"女","id":1902,"name":"软件测试2"},
    ],
    "id":19000000
}

# r = requests.post(url,data=data)
'''上面一行requests.post(url,data=data)用data参数存数据的话，取到的值都是空的。下面2种方法解决此问题'''
# 方法1（低版本python）  用dumps()解决取值为空
# r = requests.post(url,data=json.dumps(data))
#方法2（高版本python） 解决取值为空
r = requests.post(url,json=data)
print(r.text)

resp = r.json()
print("取出json串：{}".format(resp["json"]))
