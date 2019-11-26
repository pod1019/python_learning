'''
1、导入sqlite3数据库
2、创建连接sqlite3.connect()
3、创建游标对象
4、编写创建表的sql语句
5、执行sql
6、关闭游标、关闭连接
'''
# 1、导入sqlite3数据库
import sqlite3
# 2、创建连接sqlite3.connect()
con = sqlite3.connect('D:/python_learning/数据库编程/sqlite3demo/demo.db')
# 3、创建游标对象
cur = con.cursor()
# 4、编写创建表的sql语句
sql ='''create table t_person(
    pno integer primary key autoincrement,
    pname varchar not null,
    age integer 
)'''
# 5、执行sql
try:
    cur.execute(sql)
    print("创建表成功！")
except Exception as e:
    print(e)
    print("创建表失败！")

finally:
# 6、关闭游标
    cur.close()
# 关闭连接
    con.close()

