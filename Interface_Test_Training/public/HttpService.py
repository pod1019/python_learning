# 类的封装
import requests
import json
from public import Config

class MyHTTP(object):
    def __init__(self):#构造方法，初始化对象
        self.url = Config.url()

    def get(self,url,**DataAll):    #封装get请求的函数

        params = DataAll.get("params")
        headers = DataAll.get("headers")

        try:#加上异常判断
            resp = requests.get(url,params=params,headers=headers,timeout=3)
            text = resp.json()
            return text
        except Exception as e:
            print("Get错误:".format(e))

    def post(self,url,**DataAll):
        # 可以定义多个关键字参数
        params = DataAll.get("params")
        headers = DataAll.get("headers")
        data = DataAll.get("data")
        json = DataAll.get("json")
        files = DataAll.get("files")
        # 用例中用到的参数就传进来，用不到的不用传，直接调用下面这个rrequests.post(url, params=params,headers=headers,data=data,json=json,files=files)
        try:#加上异常判断
            resp = requests.post(url, params=params,headers=headers,data=data,json=json,files=files)
            text = resp.json()
            return text
        except Exception as e:
            print("POST错误:".format(e))

