# _*_ coding: utf-8 _*_

"""
数据模型
"""

import datetime
from typing import Any

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

    def __init__(self, name, email, phone, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.name = name
        self.email = email
        self.phone = phone
