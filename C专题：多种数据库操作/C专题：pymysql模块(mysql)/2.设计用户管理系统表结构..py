# _*_ Anaconda3-Python3.8 _*_
import pymysql


def create_table():
    cursor.execute("create table user_info("
                   "id int primary key auto_increment not null,"
                   "username varchar(32),"
                   "password varchar(64)) "
                   "default charset=utf8;"
                   )
    conn.commit()
    cursor.close()
    conn.close()


def login():
    print("----用户登录----")
    usr = input("用户名：")
    pwd = input("密码：")
    cursor.execute("select * from user_info where username='{}' and password='{}'".format(usr, pwd))
    tf = cursor.fetchone()  # 如果不存在，则为空，存在则获取当前登录信息
    if tf:
        print("登录成功！")
    else:
        print("用户不存在，请先注册！")


def register():
    print("----用户注册----")
    username = input("用户名：")
    password = input("密码：")
    # 有sql注入的风险
    cursor.execute("insert into user_info(username,password) values('{}','{}')".format(username, password))
    conn.commit()
    print("注册成功！")


if __name__ == '__main__':
    # 游标创建
    conn = pymysql.connect(
        host='192.168.127.140',
        port=3306,
        user='root',
        password='数据库密码',
        charset='utf8',
        db='userdb'
    )
    cursor = conn.cursor()

    # 创建表，执行一次即可
    # create_table()

    while True:
        print("-----------------")
        print(" 1.登录", "2.注册")
        print("-----------------")
        choice = input("请选择：")
        if choice == "1":
            login()
        elif choice == "2":
            register()
        else:
            continue
    cursor.close()
    conn.close()
