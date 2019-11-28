# 导入pymysql
import pymysql
# 创建连接
con = pymysql.connect(host='localhost',user='root',password='root',database='python_db',port=3306)
# 创建游标对象
cur = con.cursor()
# 编写创建表sql
sql = """
        create table t_student(
            sno int primary key auto_increment,
            sname varchar(30) not null,
            age int(2),
            score float(3)
)"""
# 执行创建表的sql
try:
    cur.execute(sql)
    con.commit()
    print("创建表成功")
except Exception as e:
    print(e)
    con.rollback()
    print("创建表失败")
# 关闭游标及连接
finally:
    # 关闭游标
    cur.close()
    # 关闭连接
    con.close()