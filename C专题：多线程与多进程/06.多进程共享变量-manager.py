# _*_ coding: utf-8 _*_

"""
功能：
"""

from multiprocessing import Manager, Process


def func1(manager):
    manager["AAA"] = 0
    print(manager)


def func2(manager):
    manager["CCC"] = "ccc"
    print(manager)


if __name__ == '__main__':
    ddd = {
        "AAA": "aaa",
        "BBB": "bbb"
    }
    manager = Manager().dict(ddd)
    p1 = Process(target=func1, args=(manager,))
    p2 = Process(target=func2, args=(manager,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
