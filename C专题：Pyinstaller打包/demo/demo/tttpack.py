# _*_coding: utf-8 _*_

"""
功能：
"""

from importlib import import_module

ttt = import_module("utils.util")  # 包名.文件名
print(ttt.get_num())
