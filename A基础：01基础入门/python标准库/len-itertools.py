# -*- coding: utf-8 -*-

"""
功能：迭代对象处理
Python的itertools模块是一个非常有用的工具，它提供了一组用于迭代器和生成器的函数。
1. 生成排列和组合：itertools.permutations()和itertools.combinations()函数可以生成给定序列的所有排列和组合。
2. 生成笛卡尔积：itertools.product()函数可以生成多个序列的笛卡尔积。
3. 生成无限迭代器：itertools.count()和itertools.cycle()函数可以生成无限迭代器，前者可以生成一个从指定数字开始的无限递增序列，后者可以生成一个无限循环的序列。
4. 迭代器切片：itertools.islice()函数可以对迭代器进行切片操作。
5. 生成压缩序列：itertools.compress()函数可以根据一个布尔序列来筛选另一个序列中的元素。
6. 生成分组序列：itertools.groupby()函数可以将一个序列按照指定的键进行分组，并返回一个生成器。
7. 生成迭代器排列组合：itertools.permutations()和itertools.combinations()函数可以生成给定序列的所有排列和组合，而itertools.product()函数可以生成多个序列的笛卡尔积。这些函数可以组合使用来生成迭代器排列组合。
"""
from itertools import permutations

x = "ABCDEFGHHA"
y = permutations(x)
print(type(y))
print(len(set(y)))
