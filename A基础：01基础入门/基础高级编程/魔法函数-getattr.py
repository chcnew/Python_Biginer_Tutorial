# _*_ coding: utf-8 _*_

"""
功能：
类的属性函数__getattr__与__getattribute__对比：
触发时机:
    __getattr__: 当访问一个不存在的属性时触发。也就是说，它只有在属性不存在的情况下才会被调用。
    __getattribute__: 在访问任何属性时都会被调用，无论属性是否存在。这个方法在属性被访问时都会被调用，而不仅仅是在属性不存在时。
调用方式：
    __getattr__: 通过点号访问属性时触发，例如 obj.attribute
    __getattribute__: 无论是通过点号还是通过函数getattr()访问属性时都会触发。
"""


class MyTTT:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # def __getattribute__(self, item):
    #     """
    #     计算“.”时执行的逻辑代码
    #     :param item: 表示后面的字符串
    #     :return:
    #     """
    #     return item

    def __getattr__(self, item):
        return item


ttt = MyTTT("chc", 28, 1)
print(ttt.name)
