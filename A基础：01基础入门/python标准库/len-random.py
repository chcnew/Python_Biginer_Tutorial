# _*_ coding: utf-8 _*_

"""
功能：
"""

import random

slist = ["A", "B", "C", "D", ["1", "2"], "E"]

aran1 = random.choice(slist)
print(aran1)

aran2 = random.choices(slist)
print(aran2)
