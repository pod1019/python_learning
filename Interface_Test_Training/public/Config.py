# 把常用的配置放到这个文件里。
# 比如url每个测试用例都用到了，那就在此写一次，在其他用例里调用即可
# 接口测试时，会在不同环境中测试，在此就可以切换环境。比如定义url1（测试环境）, url2（预发布环境）,url3,等等
def url():
    url = 'http://httpbin.org/'
    return url

# 数据库连接串
sql_conn_dict ={
    'host':'localhost',
    'user':'root',
    'passwd':'root',
    'db':'test',
    'charset':'utf8'
}