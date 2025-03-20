# -*- coding:utf-8 -*-

"""
单例模式
"""


class GeneratLog:
    def __new__(cls, *args, **kwargs):
        # 如果已经存在实例，那么返回该实例
        if not hasattr(GeneratLog, "_instance"):
            GeneratLog._instance = object.__new__(cls)
        return GeneratLog._instance


gg = GeneratLog()
gk = GeneratLog()
print(gg)
print(gk)
