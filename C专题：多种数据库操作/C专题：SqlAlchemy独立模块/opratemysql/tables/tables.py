# coding: utf-8
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    name = Column(String(64), unique=True)
    email = Column(String(64))
    phone = Column(String(11), nullable=False, unique=True)
    id = Column(INTEGER(11), primary_key=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, index=True)
    deleted_at = Column(DateTime)
