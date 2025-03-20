# _*_ coding: utf-8 _*_

"""
功能：理解元类
问题引入：metaclass是什么，有什么用？
        metaclass是创建类作为对象的一种更上级的类型，可以实现在创建对象的中间过程可以实现自定义的一些功能
"""


class Foo:
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        _instance = object.__new__(cls)
        return _instance
