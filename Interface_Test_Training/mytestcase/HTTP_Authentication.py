import requests
'''1、basic基础的认证 '''
# 方法1
r = requests.get('http://httpbin.org/basic-auth/user/passwd',auth= ('user','passwd'))
print(r.text)
# 方法2 复杂一点
from requests.auth import HTTPBasicAuth
r1 = requests.get('http://httpbin.org/basic-auth/user/passwd',auth= HTTPBasicAuth('user','passwd'))

print(r1.text)

'''2、Digest方式   MD5加密方式'''
from requests.auth import HTTPDigestAuth
r2 = requests.get('http://httpbin.org/digest-auth/user/passwd/MD5',auth= HTTPDigestAuth('user','passwd'))
print(r2.text)