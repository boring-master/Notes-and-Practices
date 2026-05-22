# from pymysql import Connection
# conn = Connection(
#     host="localhost",
#     port=3306,
#     user="root",
#     password=""
# )
# cursor = conn.cursor()
# conn.select_db('world')
# cursor.execute("insert into student values(10001,'总经理',31,'男')")
# conn.commit()
# conn.close()

from pymysql import Connection
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="",
    autocommit=True         # 自动提交（确认）
)
cursor = conn.cursor()
conn.select_db('world')
cursor.execute("insert into student values(10002,'辣椒酱',31,'男')")
conn.close()