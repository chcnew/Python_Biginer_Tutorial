# _*_ Anaconda3-Python3.8 _*_
import pymysql

# （socket方式实现连接）
conn = pymysql.connect(
    host='192.168.127.140',  # ip
    port=3306,  # 整型数据
    user='root',  # 用户
    password='数据库密码',  # 密码
    charset='utf8',  # 编码格式
    db='mytest',  # 设置默认连接数据库相当于指令use mytes;
)
# 获取游标对象
cursor = conn.cursor()
# print(cursor)  # <pymysql.cursors.Cursor object at 0x00000126883FEA90>

# 发送指令execute
cursor.execute("show databases")
# 返回数据
result = cursor.fetchall()  # 获取查看数据需要使用
# 返回存在的数据库
# print(result)
# 创建数据库
cursor.execute("create database dbname default charset utf8 collate utf8_general_ci")
conn.commit()  # 修改、删除、新增数据需要使用

# 删除数据库
cursor.execute("drop database dbname")
conn.commit()

# # 进入数据库查看表
cursor.execute("use mysql")
cursor.execute("show tables")
res = cursor.fetchall()
print(res)

# 关闭游标
conn.close()
cursor.close()
