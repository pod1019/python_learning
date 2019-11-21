import requests
import json

url = "http://116.62.198.141:9091/product/getCompanyInfoByProjectId"

payload = "obj=%7B%22appid%22%3A%2230016687%22%2C%22version_num%22%3A%226.0.0%22%2C%22module%22%3A%22product%22%2C%22mothed%22%3A%22getCompanyInfoByProjectId%22%2C%22projectId%22%3A%2219539%22%2C%22token%22%3A%22c5d1281e6d6809c7bf4c018c42250dba%22%7D"
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    #'cache-control': "no-cache",
    #'Postman-Token': "269ceb79-a280-4ab8-9262-b951917348fe"
    }

response = requests.request("POST", url, data=payload, headers=headers)

# json.dumps(response)
print(json.dumps(response.json(),indent=4))


li = ['2','3']


