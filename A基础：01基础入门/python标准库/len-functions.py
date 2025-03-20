# _*_ coding: utf-8 _*_

"""
功能：工具函数
from functools import reduce
    function -- 函数，有两个参数
    iterable -- 可迭代对象
    initializer -- 可选，初始参数
"""
from functools import reduce


def func(x, y):
    return x + y


if __name__ == '__main__':
    # result = reduce(func, [1, 2, 3, 4, 5])
    result = reduce(lambda x, y: x * 2 + y, [1, 2, 3, 4, 5])
    print(result)
