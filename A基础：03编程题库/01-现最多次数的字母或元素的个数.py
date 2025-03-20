# _*_ coding: utf-8 _*_

"""
功能：20231019面试题目
     创建一个函数输入字母或数字组成的字符串，返回其中出现最多次数的字母或元素的个数
     1.不区分大小写
     2.不满足条件的返回0
"""


def func(text: str) -> int:
    """func"""
    if text == "" or not text.isalnum():
        return 0
    result_list = []
    for i in set(list(text)):
        count = 0
        for j in text:
            if i == j:
                count += 1
        result_list.append(count)
    return max(result_list)


if __name__ == '__main__':
    print(func("aabbeeec2344565666666w"))
