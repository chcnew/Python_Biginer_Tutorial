# _*_ Anaconda3-Python3.8 _*_
import pymysql
from pymysql import cursors
from dbutils.pooled_db import PooledDB

# 全局变量
POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=50,  # 连接池允许的最大连接数, o和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=3,  # 链接池中最多闲置的链接，o和None不限制
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待;False，不等待然后报错
    setsession=[],  # 开始会话前执行的命令列表。如:[ "set datestyle to ..." ,"set time zone ..."]
    ping=0,  # ping MySQL服务端,检查是否服务可用。
    # 如: 0 = None = never, 1 = default = whenever it is requested,
    # 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    host='192.168.127.140',
    port=3306,
    user='root',
    password='数据库密码',
    database='mywork',
    charset='utf8'
)


class Connect(object):
    def __init__(self):
        # 连接池中取一个连接
        self.conn = conn = POOL.connection()
        self.cursor = conn.cursor(cursors.DictCursor)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

    # 定义操作方法
    def exec(self, sql, **kwargs):
        self.cursor.execute(sql, kwargs)
        self.conn.commit()

    def fetch_one(self, sql, **kwargs):
        self.cursor.execute(sql, kwargs)
        return self.cursor.fetchone()

    def fetch_all(self, sql, **kwargs):
        self.cursor.execute(sql, kwargs)
        return self.cursor.fetchall()
