import requests
'''代理用的比较少，知道有proxies这么个参数就行'''
'''1、代理配置'''
proxies = {
    'http':'http://10.10.1.10:3128',
    'https':'https://10.10.1.10:1080',
}

requests.get('http://example.org',proxies=proxies)  #当访问http://example.org网站的时候，就会通过代理服务器访问了
'''2、设置环境变量'''
# $ export = HTTP_PROXY='http://10.10.1.10:3128'
# $ export = HTTPS_PROXY='http://10.10.1.10:1080'
# $ python
# requests.get('http://example.org')

'''3、若你的代理需要使用HTTP Basic Auth，可以用 http://user:password@host/ 语法'''
proxies = {
    'http':'http;//user:pass@10.10.1.10:3128/',
}

'''4、要为某个特定的连接方式或者主机设置代理，使用 scheme://hostname作为 key, 
他会针对指定的主机和连接方式进行匹配
'''
proxies = {'http://10.10.1.128':'http://10.10.1.10:5323'}

'''5、SOCKS'''
proxies = {
    'http':'socks5://user:pass@host:port',
    'https':'socks5://user:pass@host:port',
}

