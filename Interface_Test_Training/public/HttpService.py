import requests
import json
from public import Config

class MyHTTP():
    def __init__(self):
        self.url = Config.url()

    def get(self,url,params):
        resp = requests.get(url,params=params)
        text = resp.json()
        return text