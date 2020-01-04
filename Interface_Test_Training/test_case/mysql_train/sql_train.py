import pymysql
from public import Config
'''1创建连接'''
conn = pymysql.connect(**Config.sql_conn_dict)
'''2创建游标，用作操作数据库'''
cur = conn.cursor()

'''数据库操作'''

# sql = 'select * from student'
# cur.execute(sql)
# print(cur.fetchone())
# print(cur.fetchone())
# # cur.scroll(0,mode='absolute') # 绝对移动：把游标移动到初始位置
# cur.scroll(-1,mode='relative')# 相对移动：把游标从当前位置移动到上1行的位置（当前位置线上移动n行，用-n）
# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchmany(2)) # 取下面两行
# print(cur.fetchall()) # 取剩余的所有行
'''
code=1
写法1
# sql = "select * from student where code = %s" %code
# cur.execute(sql)
# 写法2   比写法1更好，能防止SQL注入
sql = "select * from student where code = %s"
cur.execute(sql,code)  #把code作为参数传入
'''


# 多个参数
code = (('女','18'),('man','19')) #sex字段和age字段.这样写也能防止SQL注入
sql = "select * from student where sex = %s and age = %s"
cur.executemany(sql,code) #多个参数 必须要用executemany
print(cur.fetchone())
'''关闭游标、关闭连接'''
cur.close()
conn.close()
