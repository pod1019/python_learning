import requests
from lxml import etree
s = requests.session()
def get_it_execution():
    result = {}

    loginurl = 'https://account.chsi.com.cn/passport/login'
    h1 = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
    s.headers.update(h1)
    r = s.get(loginurl,verify=False)
    # params = {
    #     'username':13911094401,
    #     'password':'fjj1983210'
    # }
    # r = requests.post(url=url,params=params)
    print(r.text)