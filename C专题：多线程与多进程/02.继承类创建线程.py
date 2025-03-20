#!/bin/bash/python3
# _*_ coding: utf-8 _*_
import threading
from threading import Thread


class MyThread(Thread):
    """自定义线程类"""

    def __init__(self, num):
        super().__init__()
        self.total = 0
        self.num = num

    def run(self) -> None:
        """start方法自动运行的函数"""
        for i in range(self.num):
            self.total += i
        print(self.total)


def task():
    # 获取当前执行该函数的线程名称
    name = threading.current_thread().getName()
    print(name)


thread1 = MyThread(100000)
thread2 = MyThread(10000)
thread3 = threading.Thread(target=task)
# thread2.name = "t2"
# thread2.daemon = True
# 获取当前执行此代码的线程名称
name = threading.current_thread().getName()
print(name)
thread2.start()
thread2.join()
thread1.start()
thread1.join()
thread3.start()
thread3.join()