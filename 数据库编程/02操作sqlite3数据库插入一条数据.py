# 导入模块
import sqlite3
# 创建连接
con = sqlite3.connect('D:/python_learning/数据库编程/sqlite3demo/demo.db')
# 创建游标对象
cur = con.cursor()
# 编写插入sql
# 由于pno设置的是自增，所以不需要在写，values(?,?)用?占位
sql = 'insert into t_person(pname,age) values (?,?)'

# 执行插入一条数据的sql
try:
    # 插入一条数据用元组的形式，把值用元组包起来----注意与插入多条数据的区别，多条用列表
    cur.execute(sql,("张三",24))
    con.commit() # 提交
    print("插入一条数据成功")
except Exception as e:
    print(e)
    con.rollback() #插入不成功，则回滚
    print("插入一条数据失败")
finally:
    # 关闭游标
    cur.close()
    # 关闭数据库连接
    con.close()
