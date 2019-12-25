import requests

host = 'https://httpbin.org/'
endpoint = 'cookies'
url = ''.join([host,endpoint])
url1 = 'http://www.baidu.com/'

r = requests.get(url)
print(r.cookies) #获取cookies。打印结果是<RequestsCookieJar[]>
print(r.text)
d = requests.utils.dict_from_cookiejar(r.cookies) #把jar包转换成字典 <RequestsCookieJar[]>是一个伪字典的形式

'''获取cookies'''
# 通过字典去迭代 获取cookies
print({a.name:a.value for a in r.cookies}) #通过字典去迭代，取出cookies的值

'''发送cookies'''
#向server发送cookies
# 1、简单方式
cookies = {'cookies-name':'jjtest','cookies-name1':'jjtest1'} #把cookies放到字典里
r1 = requests.get(url,cookies=cookies) #把自定义的cookies传给关键字参数cookies
print(r1.text)

# 2、复杂的方式，但常用
s = requests.session() #添加cookies时，必须要保持session会话
c = requests.cookies.RequestsCookieJar()

# 通过set()设置cookies的名称和值；通过path指定路径，通过domain设置服务器地址
c.set('cookies-name2','qiaoba',path='/',domain = '.test.com')
s.cookies.update(c) # 把cookies通过update(c)传给session (s)
print(s.cookies)
