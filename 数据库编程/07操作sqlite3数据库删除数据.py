# 导入模块
import sqlite3
# 创建连接
con = sqlite3.connect('D:/python_learning/数据库编程/sqlite3demo/demo.db')
# 创建游标对象
cur = con.cursor()
# 编写删除sql
delete_sql = 'delete from t_person where pno=?'

try:
    # 执行sql
    cur.execute(delete_sql,(8,))
    # 提交事务
    con.commit() #修改成功，则提交事务
    print("删除成功")
except Exception as e:
    print(e)
    con.rollback() #修改失败，则回滚事务
    print("删除失败")
finally:
    # 关闭游标
    cur.close()
    # 关闭连接
    con.close()