# _*_ coding: utf-8 _*_

"""
功能：
"""
import time
from multiprocessing import Process

from g_params import cbool


def workfunc():
    print(2, cbool.value)
    cbool.value = False
    print(3, cbool.value)
    time.sleep(5)


if __name__ == '__main__':
    print(1, cbool.value)
    p = Process(target=workfunc)
    p.start()
    print(4, cbool.value)
    while cbool.value:
        time.sleep(1)
    print(5, cbool.value)
