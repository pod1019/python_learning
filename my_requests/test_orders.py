# -*- coding: utf-8 -*-
__author__ = "FTest"
import requests
import json
url = "https://open.caituketang.com/orders/createOrder"

postdata = {
    'productType':'52',
    'productId':'122',
    'buyQty':'1'
}
myheaders = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin' : 'http://m.caituketang.com',
    'Referer': 'http://m.caituketang.com/consultation_my.html',
    'token': 'H7FnP6PmtADh7Gr6SRqQ5QpwptmjX0ib7hiComT3GYnOvH0PqkaNzOphr8b7EQ75QsbyISc93ImfbEnEJ3YVw8KAlIHvg+UR/4ZsrgLomvd7X5sonadX4Z7UVTPgdpDiP7WWhGECdkGuL4acVpzZVHO3HUspdBCEw2jY9Y59BDZxGdHkdRpynYn0hSULTnsCkYhB7uejsUkpLo7APIFEEu79FVCCJ3ARVhvIBfr5UNHll4q/KvB7Eyg5VBdhqJrm+0cxNuiWcsjmJFHZdIBp4w==',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
}

resp = requests.request("post",url,data = postdata,headers=myheaders)

print(json.dumps(resp.json(),indent=4))