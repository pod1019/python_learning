# 导入模块
import sqlite3
# 创建连接
con = sqlite3.connect('D:/python_learning/数据库编程/sqlite3demo/demo.db')
# 创建游标对象
cur = con.cursor()
# 编写修改数据sql
update_sql = 'update t_person set pname=? where pno=?'

try:
    # 执行sql
    cur.execute(update_sql,('小张',3))
    # 提交事务
    con.commit() #修改成功，则提交事务
    print("修改成功")
except Exception as e:
    print(e)
    con.rollback() #修改失败，则回滚事务
    print("修改失败")
finally:
    # 关闭游标
    cur.close()
    # 关闭连接
    con.close()