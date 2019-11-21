import requests
import json
url = 'https://open.yuanin.com/flkt/user/login'
obj = {
    'mobile':'13911094401',
    'validCode':'123456',
    'appId':'20011123',
    'versionNum':'2.0'
}
def send_post(url,data=None):
    res = requests.post(url=url,data=obj)
# json.dumps(res)
    return res
    print(res)

send_post(url,obj)