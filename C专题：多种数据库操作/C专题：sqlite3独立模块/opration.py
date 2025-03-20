# _*_ coding: utf-8 _*_

"""
功能：sqlite3操作
"""
import sqlite3

DB = './example.db'


def test1_create_and_insert():
    # 连接到SQLite数据库文件（不存在则会自动创建）
    with sqlite3.connect(DB) as conn:
        # 创建一个游标对象
        cursor = conn.cursor()
        # 创建一个示例表
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
            )
            '''
        )
        # 插入一条数据 / 参数化查询来插入数据，这样可以防止SQL注入攻击
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("魏大勋", 30))
        # 提交事务
        conn.commit()
        # 关闭游标
        cursor.close()


def test2_insert():
    # 连接到SQLite数据库
    with sqlite3.connect(DB) as conn:
        # 创建一个游标对象
        cursor = conn.cursor()
        # 插入一条数据
        sql = "INSERT INTO users (name, age) VALUES (?, ?)"
        data = ('钟无艳', 25)
        cursor.execute(sql, data)
        # 提交事务
        conn.commit()
        # 关闭游标和连接
        cursor.close()


def test3_query():
    # 连接到SQLite数据库
    with sqlite3.connect(DB) as conn:
        # 创建一个游标对象
        cursor = conn.cursor()
        # 插入一条数据
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        # 获取查询结果
        results = cursor.fetchall()
        for row in results:
            print('\n', row)
        # 提交事务
        conn.commit()
        # 关闭游标和连接
        cursor.close()


def test4_update():
    # 查询更新前数据
    with sqlite3.connect(DB) as conn:
        # 创建一个游标对象
        cursor = conn.cursor()
        query_sql = "select * from users where name = ?"
        query_data = ("魏大勋",)  # 就算只有一个值，也必须用元组包裹
        cursor.execute(query_sql, query_data)
        results = cursor.fetchall()
        print("\n[更新前数据]：", results)
        # 更新一条数据
        update_sql = "update users set age = ? where name = ? AND id = ?"
        update_data = (54, "魏大勋", 2)
        cursor.execute(update_sql, update_data)
        # 提交事务
        conn.commit()
        # 查询更新后数据
        cursor.execute(query_sql, query_data)
        results = cursor.fetchall()
        print("[更新后数据]：", results)
        # 关闭游标
        cursor.close()


def test5_delete():
    with sqlite3.connect(DB) as conn:
        # 创建一个游标对象
        cursor = conn.cursor()
        # 删除一条数据
        delete_sql = "DELETE FROM users WHERE name = ? AND id = 1"
        data = ('魏大勋',)
        cursor.execute(delete_sql, data)
        # 提交事务
        conn.commit()
        # 关闭游标
        cursor.close()
