## **Pymysql&mysql学习笔记**
### 一、数据库连接及基本操作
```python
import pymysql

# （socket方式实现连接）
conn = pymysql.connect(
    host='192.168.127.140',  # ip
    port=3306,  # 整型数据
    user='root',  # 用户
    password='Cc158854@',  # 密码
    charset='utf8',  # 编码格式
)
# 获取游标对象
cursor = conn.cursor()
# print(cursor)  # <pymysql.cursors.Cursor object at 0x00000126883FEA90>

# 发送指令
cursor.execute("show databases")
# 返回数据
result = cursor.fetchall()  # 获取查看数据需要使用
# 返回存在的数据库
print(result)
# 创建数据库
cursor.execute("create database dbname default charset utf8 collate utf8_general_ci")
conn.commit()  # 修改、删除、新增数据需要使用

# 删除数据库
cursor.execute("drop database dbname")
conn.commit()

# 进入数据库查看表
cursor.execute("use mysql")
cursor.execute("show tables")
result = cursor.fetchall()
print(result)

# 关闭游标
conn.close()
cursor.close()
```

### 二、用户管理系统登陆注册表结构设计
#### 1.创建数据库
```mysql
create database userdb default charset utf8 collate utf8_general_ci
```

#### 2.创建表结构(pymysql)
```mysql
create table user_info(
    id int primary key auto_increment not null,
    username varchar(32),
    password varchar(64)
) default charset=utf8;
```