#!/bin/bash/python3
# _*_ coding: utf-8 _*_

"""
两个线程启动，虽说保证主线程等待子线程运行完毕后再继续，
但两个子线程之间存在操作同一个变量的情况，这时候就需要
使用同一把锁，谁先获得锁线谁就先执行完毕后，才到另外一个。
"""

import time
from threading import Thread, RLock

total = 0
rlock = RLock()


def func1():
    rlock.acquire()
    global total
    for i in range(100000):
        total += i
    rlock.release()


def func2():
    with rlock:
        global total
        for i in range(100000):
            total -= i


t1 = Thread(target=func1)
t2 = Thread(target=func2)
t1.start()  # t1线程启动
t2.start()  # t2线程启动
# t1.join()  # t1执行完主线程才继续往后
# t2.join()  # t2执行完主线程才继续往后

# 不使用join方式，使用锁的方式运行全部，此处sleep是为了等子线程运行完成
time.sleep(1)
print(total)
