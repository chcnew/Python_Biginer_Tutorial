# _*_encoding: utf-8 _*_

"""
功能：MYTTT
"""

import time

while n > 8:
    print('T-minus', n)
    n -= 1
    time.sleep(5)

from threading import Thread

t = Thread(target=countdown, args=(10,))
