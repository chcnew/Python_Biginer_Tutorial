# coding: utf-8

import threading
import time


def func1():
    print('我去你')
    time.sleep(5)


def func2():
    print('大爷！')
    time.sleep(5)


try:
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)

    t1.start()
    t2.start()
except Exception as e:
    print(e)

# 以上代码执行只需5秒多一点点，说明多线程生效
# 按照单线程处理应该需要10多秒。
