#!/bin/bash/python3
# _*_ coding: utf-8 _*_

import os
from setuptools import setup, find_namespace_packages

setup(
    name='ucmtools',  # 应用名
    author='chc',  # 作者
    version='0.0.1',  # 版本号
    packages=find_namespace_packages(),  # 包括在安装包内的Python包及文件夹
    install_requires=[  # 自动安装依赖
        'PySide2>=5.15.2.1',
        'pytest>=7.2.0',
        'pytest-html>=3.2.0',
    ],
)
