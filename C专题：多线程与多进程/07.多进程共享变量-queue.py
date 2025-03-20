# _*_ coding: utf-8 _*_

"""
功能：
"""

import time
from multiprocessing import Process, Queue


def generate_data(queue: Queue):
    """generate_data"""
    for i in range(10):
        queue.put(i)


def consumer_data(queue: Queue):
    """consumer_data"""
    while not queue.empty():
        print(queue.get())
        time.sleep(1)


if __name__ == '__main__':
    queue = Queue()
    p1 = Process(target=generate_data, args=(queue,))
    p2 = Process(target=consumer_data, args=(queue,))
    p1.start()
    p2.start()
    p2.join()
