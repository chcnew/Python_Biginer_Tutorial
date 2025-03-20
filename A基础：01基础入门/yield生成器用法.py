# _*_ coding: utf-8 _*_

"""
功能：yield实现斐波那契数列
"""


def generator():
    i = 0
    j = 1
    while i < 4:
        yield i
        i, j = j, i + j


ttt = generator()
# result = sum(ttt)
# print(result)
for item in ttt:
    print(item)
