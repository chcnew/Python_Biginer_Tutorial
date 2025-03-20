# -*- coding: utf-8 -*-

"""
功能：装饰器里面的外层变量定义字典,里面存放这个类的实例.当第一次创建的时候,就将这个实例保存到这个字典中.
然后以后每次创建对象的时候,都去这个字典中判断一下,如果已经被实例化,就直接取这个实例对象.如果不存在就保存到字典中.
"""

from functools import wraps


def singleton(cls):
    _instance = {}

    @wraps(cls)
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@singleton
class A:
    def __int__(self):
        self.xxx = "xxx"
        self.yyy = "yyy"


class Data:
    a1 = None
    a2 = None
    b1 = None
    b2 = None


if __name__ == '__main__':
    a = A()
    b = A()
    print(a.__class__.__name__, id(a))
    print(b.__class__.__name__, id(b))
