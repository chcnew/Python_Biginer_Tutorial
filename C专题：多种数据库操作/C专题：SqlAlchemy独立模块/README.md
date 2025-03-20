# SqlAlchemy独立模块



## 一、部署

### 1.rpm安装

```shell
#!/bin/bash

# rpm -e mysql-community*

rpm -ivh mysql-community-common-5.7.42-1.sles12.x86_64.rpm
rpm -ivh mysql-community-libs-5.7.42-1.sles12.x86_64.rpm
rpm -ivh mysql-community-client-5.7.42-1.sles12.x86_64.rpm
rpm -ivh mysql-community-server-5.7.42-1.sles12.x86_64.rpm
rpm -ivh mysql-community-devel-5.7.42-1.sles12.x86_64.rpm
rpm -ivh mysql-community-embedded-5.7.42-1.sles12.x86_64.rpm
rpm -ivh mysql-community-embedded-devel-5.7.42-1.sles12.x86_64.rpm
rpm -ivh mysql-community-test-5.7.42-1.sles12.x86_64.rpm
```

### 2.密码设置

```shell
vim /etc/my.cnf
#无密码登录
#skip-grant-tables
#启动服务
systemctl start mysql
#修改密码
mysql
use mysql;
update user set authentication_string='123456' where user='root';
flush privileges;
#重启服务
systemctl restart mysql
#再次使用密码登录
mysql -uroot -p 
```

### 3.远程登录

```mysql
mysql -uroot -p

use mysql;
select host,user from user;
update user set Host='%' where User='root';
flush privileges;
```

### 4.sqlalchemy操作数据库

```shell
pip3 install sqlalchemy alembic pymysql sqlacodegen 
```

​	**oprate_mysql.py**

```python
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

```

​	**config.py**

```python
# _*_ coding: utf-8 _*_

"""
配置文件
"""

URI = "mysql+pymysql://root:Cc158854%40@192.168.127.140/learn_sqlalchemy?charset=utf8mb4"


class Config:
    """Config"""
    SQLALCHEMY_DATABASE_URI = URI
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_POOL_SIZE = 6
    SQLALCHEMY_POOL_MAX_SIZE = 8
    SQLALCHEMY_POOL_RECYCLE = 60 * 30

```

​	**models/model.py**

```python
# _*_ coding: utf-8 _*_

"""
数据模型
"""

import datetime

from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseMixin:
    """model的基类,所有model都必须继承"""
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now, index=True)
    deleted_at = Column(DateTime)  # 可以为空, 如果非空, 则为软删


class User(Base, BaseMixin):
    __tablename__ = "user"

    name = Column(String(64), unique=True)
    email = Column(String(64))
    phone = Column(String(11), nullable=False, unique=True)

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

```

**使用alembic操作数据库迁移**

参考文档：

​	https://blog.csdn.net/chichu261/article/details/87307773

​	https://hellowac.github.io/technology/python/sqlalchemy/

```shell
# 建立文件
python -m alembic init alembic

# 修改配置文件：alembic.ini
sqlalchemy.url = mysql+pymysql://root:Cc158854%%40@192.168.127.140/learn_sqlalchemy

# env.py
from ..models.model import Base
target_metadata = Base.metadata

# 提交迁移（注意运行路径）
python -m alembic revision --autogenerate -m "initdb"
python -m alembic upgrade head  # 升级到最新版本
```

### 5.模型逆向工具：sqlacodegen

数据库 -> tables.py

```shell
sqlacodegen --tables alembic_version,user mysql+pymysql://root:Cc158854%40@192.168.127.140:3306/learn_sqlalchemy --outfile tables.py
```



## 二、应用

