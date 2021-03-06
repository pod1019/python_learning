# 导入模块
import sqlite3
# 创建连接
con = sqlite3.connect('D:/python_learning/数据库编程/sqlite3demo/demo.db')
# 创建游标对象
cur = con.cursor()
# 编写查询sql
sql = 'select * from t_person'

try:
    # 执行sql，
    cur.execute(sql)
    # 获取结果集
    person_all = cur.fetchall()
    for person in person_all:
        # print(person_all)
        print(person)
except Exception as e:
    print(e)
    print("查询多条数据失败")
finally:
    # 关闭游标
    cur.close()
    # 关闭连接
    con.close()