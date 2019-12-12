import requests
import json

class RunMain:
    #
    def send_post(self,url,data):
        result = requests.post(url=url,data=data).json()
        res = json.dumps(result,sort_keys=True,indent=4)
        return res
    def send_get(self,url,data):
        result = requests.get(url=url,data=data).json()
        res = json.dumps(result,sort_keys=True,indent=2)


    def run_main(self,method,url=None,data=None):
        result = None

        if method == "post":
            result=self.send_post(url,data)

        elif method == "get":
            result=self.send_post(url,data)
        else:
            print('不是这两种借口')
        return result