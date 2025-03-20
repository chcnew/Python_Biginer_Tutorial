# _*_ Anaconda3-Python3.8 _*_
import pymysql
from pymysql import cursors
from dbutils.pooled_db import PooledDB

MYSQL_DB_POOL = PooledDB(
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


def task():
    # 连接池中取一个连接
    conn = MYSQL_DB_POOL.connection()
    cursor = conn.cursor(cursors.DictCursor)
    cursor.execute('select sleep(2)')
    result = cursor.fetchall()
    print(result)

    # 关闭游标，将连接交给连接池
    cursor.close()
    conn.close()


if __name__ == '__main__':
    task()
