import requests
import unittest
class GetNothingTest(unittest.TestCase):
    '''get无参数测试'''
    # 1、定义setUp方法
    def setUp(self):
        host = 'https://httpbin.org/'
        endpoint = 'get'
        self.url = ''.join([host,endpoint])

    def test1(self):
        '''校验状态码是否为200'''
        r = requests.get(self.url)
        # print(r.url) #获取URL
        print(r.status_code,r.reason) #r.status_code获取响应状态码,r.reason获取状态码的原因

        #下面两个方式 展现形式不一样。可以通过查看类型，是不一样的
        print(r.text) #unicode 文本
        print(type(r.text)) #查看r.text的类型 <class 'str'>
        print(r.content) #bytes 图片、文件等
        print(type(r.content)) #查看r.content类型 <class 'bytes'>

        print('我是响应头:',r.headers) #响应头
        print('我是请求头:',r.request.headers) #这个是请求头（是响应中把request属性的一些信息被带过来，比如请求头）
        # 获取请求头的其他信息，比如url、method  不常用，用于调试
        print(r.request.url)
        print(r.request.method)
        print(r.text) #unicode 文本
        print(type(r.text)) #查看r.text的类型 <class 'str'>
        print(r.content) #bytes 图片、文件等
        print(type(r.content)) #查看r.content类型 <class 'bytes'>

        print('我是响应头:',r.headers) #响应头
        print('我是请求头:',r.request.headers) #这个是请求头（是响应中把request属性的一些信息被带过来，比如请求头）
        # 获取请求头的其他信息，比如url、method  不常用，用于调试
        print(r.request.url)
        print(r.request.method)

        response = r.json() # 把请求响应的对象 r 变成json串 这种形式好处是可以取很多信息，比如headers ---常用
        # print(type(response))
        '''下面这种取值，在用unittest自动化测试中，常用作断言，去判定测试的实际结果和预期结果是否匹配'''
        print(response['headers']) #根据response的key 'headers'，取到headers的信息
        print(response['headers']['User-Agent']) #先取到headers信息，再取headers信息中key为'User-Agent'的值

        '''下面这种方式是取不到的，因为r.text是字符串形式，字符串只能通过下标、切片方式去取，太麻烦。
        # print(r.text['headers']['User-Agent'])
        但可以通过eval()函数,将r.text转换成字典形式eval(r.text)['headers']['User-Agent']，再通过key去取到
        '''
        print(eval(r.text)['headers']['User-Agent'])
        # print(type(eval(r.text)))
    def test2(self):
        '''校验主机域名'''
        r = requests.get(self.url)
        resp = r.json()
        Host = resp['headers']['Host']
        self.assertEqual(Host,'httpbin.org')


    def tearDown(self):
        pass


if __name__ =="__main__":
    unittest.main()


