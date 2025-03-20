# _*_ coding: utf-8 _*_

"""
操作数据库
"""
import contextlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config
from models.model import User

engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,  # SQLAlchemy 数据库连接串
    echo=bool(Config.SQLALCHEMY_ECHO),  # 是不是要把所执行的SQL打印出来，用于调试
    pool_size=int(Config.SQLALCHEMY_POOL_SIZE),  # 连接池大小
    max_overflow=int(Config.SQLALCHEMY_POOL_MAX_SIZE),  # 连接池最大的大小
    pool_recycle=int(Config.SQLALCHEMY_POOL_RECYCLE),  # 多久时间主动回收连接
)
Session = sessionmaker(bind=engine)


@contextlib.contextmanager
def get_session():
    sess = Session()
    try:
        yield sess
        sess.commit()
    except Exception as err:
        sess.rollback()
        raise err
    finally:
        sess.close()


try:
    with get_session() as sess:
        user = User("json", "123@123.com", "00000000000")
        sess.add(user)
        sess.commit()
except:
    pass

with get_session() as sess:
    for item in sess.query(User).all():
        print(item.__dict__)
