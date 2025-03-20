# _*_ coding: utf-8 _*_

"""
配置文件
"""

URI = "mysql+pymysql://root:数据库密码（@=%40）@192.168.127.140/learn_sqlalchemy?charset=utf8mb4"


class Config:
    """Config"""
    SQLALCHEMY_DATABASE_URI = URI
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_POOL_SIZE = 6
    SQLALCHEMY_POOL_MAX_SIZE = 8
    SQLALCHEMY_POOL_RECYCLE = 60 * 30
