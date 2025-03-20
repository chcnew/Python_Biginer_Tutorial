# _*_ coding: utf-8 _*_

"""
USER: Administrator
DATE: 2023/2/2
FILE: __main__.py
"""

import json
import os
import sys


def get_dirpath(dpath, num):
    """
    向上获取文件夹路径

    :param dpath: 当前路径
    :param num: 向上获取层数（0层表示当前目录）
    :return: 路径（str）
    """
    back_dir = os.path.dirname(dpath)
    if num >= 1:
        return get_dirpath(back_dir, num - 1)
    else:
        return back_dir


# abs_path = os.path.abspath(__file__)
abs_path = sys.argv
abs_path0 = sys.argv[0]
abs_path1 = sys.argv[1]
print(abs_path)
print(abs_path0)
print(abs_path1)
BASE_DIR = get_dirpath(abs_path0, 0)
print(BASE_DIR)

if __name__ == '__main__':
    config_path = os.path.join(BASE_DIR, "res", "config.json")
    with open(config_path, mode="r", encoding="utf-8") as rf:
        data = json.load(rf)
    print(data)
