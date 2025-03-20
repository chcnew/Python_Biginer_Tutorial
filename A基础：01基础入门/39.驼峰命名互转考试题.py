# -*- coding:utf-8 -*-
"""

面试官对所有人说： 03:37 PM
编写一个函数，实现驼峰式命名与下划线命名的互转

即：helloWorld <--> hello_world

testcase1: getValue, expect: get_value

testcase2: run_step1, expect: runStep1


# 转为列表，循环判断是不是大写字母，是大写字母在当前元素之前插入一个"_"
# isupper()
# upper()
# islower()
# lower()
# "".join(lst)  # 括号内为可迭代对象
"""


def to(x_str):
    lst = list(x_str)

    if "_" in x_str:
        for i in range(len(lst)):
            if lst[i] == "_":
                up = lst[i + 1].upper()
                del lst[i]
                lst.insert(i, up)
                return "".join(lst)

    else:
        for i in range(len(lst)):
            if lst[i].isupper():
                lst.insert(i, "_")
                lst[i + 1].lower()  # 转为小写
                return "".join(lst)


print(to("run_step1"))
print(to("getValue"))
