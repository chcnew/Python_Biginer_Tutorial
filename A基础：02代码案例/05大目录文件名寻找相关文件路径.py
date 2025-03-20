# -*- coding: utf-8 -*-

"""
功能：os.scandir(dir)高性能遍历文件夹（生成器）
"""

import os


def func(fdir: str, name: str):
    directorys = []
    with os.scandir(fdir) as entries:
        for entry in entries:
            if entry.name == name:
                print('File:', entry.path)
            if entry.is_dir():
                directorys.append(entry.path)
    for item in iter(directorys):
        try:
            func(item, name)
        except PermissionError:
            pass


if __name__ == '__main__':
    name = 'xxx.json'
    fdir = 'D:\\'
    func(fdir, name)
