# coding:utf-8

import pymysql

# 建立连接 ip 端口号 用户名 密码 数据库名
db = pymysql.Connect(host='106.15.194.195',
                     port=3306,
                     user='sql_cc0722',
                     passwd=r'ZMSkHypQpT{数据库密码}',
                     db='sql_cc0722',
                     charset='utf8'
                     )

# 创建游标对象
cursor = db.cursor()

print(db)
