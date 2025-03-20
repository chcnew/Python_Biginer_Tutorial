#!/bin/bash/python3
# _*_ coding: utf-8 _*_

import threading

total = 0


def func1(num):
    global total
    for i in range(num):
        total += i


t1 = threading.Thread(target=func1, args=(1000000,))
t1.start()

print(total)
