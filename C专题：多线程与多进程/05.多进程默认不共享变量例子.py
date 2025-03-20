#!/bin/bash/python3
# _*_ coding: utf-8 _*_
import time
from multiprocessing import Process
from io import StringIO

var = "0"
bio = StringIO()


def fun1():
    global var, bio
    print(var)
    var = "111"
    print(var)
    bio.write(var)
    time.sleep(3)


def fun2():
    global var, bio
    print(bio.getvalue())
    var = "222"
    print(var)


if __name__ == '__main__':
    p1 = Process(target=fun1)
    p1.start()
    p1.join()
    p2 = Process(target=fun2)
    p2.start()
