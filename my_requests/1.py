import requests
import json
url = 'http://httpbin.org/post'
# files = {'file':open('report.xlsx','rb')}
r = requests.post(url).json()
res = json.dumps(r)


print(res)

# d = {}
# print('{')
# for i in j:
#     print('\t'+i+': '+j.get(i)+',')
# print('}')

