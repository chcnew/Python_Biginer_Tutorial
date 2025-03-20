# _*_ coding: utf-8 _*_

"""
功能：
"""
import time

from init import app


@app.task
def sum(x, y):
    return x + y


@app.task
def mul(x, y):
    time.sleep(5)
    return x * y
