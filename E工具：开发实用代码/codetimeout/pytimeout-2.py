# _*_ coding: utf-8 _*_

"""
功能：eventlet超时控制代码库
"""

import time

import eventlet

eventlet.monkey_patch()  # 必须加这条代码

try:
    with eventlet.Timeout(3, True):  # 设置3秒超时、True表示异常可以被捕获
        time.sleep(10)  # 模拟一个耗时10秒的函数
except eventlet.timeout.Timeout as err:
    print(err)

print("1111")
