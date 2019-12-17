from public import Config

def get_url(EndPoint): # 用例中定义的endpoint都不一样，写在这里，怎么修改都不会影响用例，用例只要把传递参数过来
    host = Config.url()
    endpoint = EndPoint
    url = ''.join([host, endpoint])
    return url