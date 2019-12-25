'''测试post方式，上传文件'''
import requests
host = 'https://httpbin.org/'
endpoint = 'post'
url = ''.join([host,endpoint])

# 1、普通上传
# files = {'files':open('test.txt','rb')}

# 2、通过文件上传字符串等
# files = {'files':('test.txt','send ssss')} #把字符串'send ssss'通过文件方式上传

# 3、自定义文件名、文件类型以及请求头以         元组的方式（请求文件名称、文件路径、文件类型、文件请求头）
files = {'files':('修改后的名称--软件测试.jpg',open('软件测试.jpg','rb'), 'image/png',{"refer":"localhost"})}  #以元组的方式;'image/png'指定图片存储格式
# files = {'files':open('软件测试.jpg','rb')}

# 4、传送多个文件 ---列表+元组的格式
# files = [
#     ('field1',('test.txt',open('test.txt','rb'))),
#     ('field2',('软件测试.jpg',open('软件测试.jpg','rb'), 'image/png')),
# ]

# 5、流式上传

# with open('test.txt','rb') as f:
# 文件被放到data这个参数里，不是像上面4个方式，都放到files参数里。需要注意,所以需要用data参数，即data=f，而不是files=f
#     r = requests.post(url,data=f)
r = requests.post(url,files=files)
print(r.headers)
print(r.text)
