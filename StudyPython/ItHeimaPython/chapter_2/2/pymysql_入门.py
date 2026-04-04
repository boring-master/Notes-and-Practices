# from pymysql import Connection
# conn = Connection(
#     host="localhost",       # 主机名
#     port=3306,              # 端口默认3306
#     user="root",            # 账户
#     password="1598588ui%A+" # 密码
# )
# # 获取游标对象
# cursor = conn.cursor()
# # 选择数据库
# conn.select_db('test')
# # 执行sql
# cursor.execute('create table test_pymysql(id int);')
# conn.close()

from pymysql import Connection
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="1598588ui%A+"
)
cursor = conn.cursor()
conn.select_db('world')
cursor.execute('select * from student')
result = cursor.fetchall()
for r in result:
    print(r)
conn.close()

'''在dbeaver中
use world;
create table student(
	id int,
	name varchar(10),
	age int,
	gender varchar(10)
);
insert into student values(10001,'总经理',31,'男'),(10002,'网络化',33,'男'),(10003,'产业链',35,'女'),
(10004,'离职率',36,'女'),(10005,'楼栋号',33,'男'),(10006,'指导书',10,'男'),(10007,'楼中楼',11,'男'),
(10008,'危险性',33,'女'),(10009,'主页面',20,'女'),(10010,'稳压器',13,'女'),(10011,'差异性',31,'男'),
(10012,'照相馆',33,'男'),(10013,'类对象',12,'男'),(10014,'龙抬头',36,'女'),(10015,'中医院',31,'女'),
(10016,'零件号',21,'女'),(10017,'洗衣粉',23,'男'),(10018,'连点器',26,'男'),(10019,'维权群',11,'男'),
(10020,'老字号',25,'女');
'''