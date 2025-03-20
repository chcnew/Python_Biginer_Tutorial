"""
 * @Description: Python
 * @Author: chc
 * @CreateDate: 2022/3/4
 * @Version: 1.0
"""
import sys


def iterator():
    """
    迭代器
    迭代是Python最强大的功能之一，是访问集合元素的一种方式。
    迭代器是一个可以记住遍历的位置的对象。
    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束，迭代器只能往前不会后退。
    迭代器有两个基本的方法：iter() 和 next()。
    字符串，列表或元组对象都可用于创建迭代器：
    """

    lst = [1, 2, 3, 4]
    it = iter(lst)  # 创建迭代器对象

    print(next(it))  # 输出迭代器下一个元素：1
    print(next(it))  # 输出迭代器下一个元素：2
    print(next(it))  # 输出迭代器下一个元素：3
    print(next(it))  # 输出迭代器下一个元素：4
    print("\n")

    # 迭代器对象可以使用常规for语句进行遍历
    lst = [1, 2, 3, 4]
    it = iter(lst)
    for x in it:
        print(x, end=",")  # end表示尾部同时输出字符
    print("\n")

    # 使用 next() 函数实现遍历
    lst = [1, 2, 3, 4]
    it = iter(lst)
    while True:
        try:
            print(next(it))
        except StopIteration:
            sys.exit()


def fibonacci(n):  # 生成器函数 - 斐波那契：0 1 1 2 3 5 8 13 21 34 55
    """
    在 Python 中，使用了 yield 的函数被称为生成器（generator）。
    跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
    在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
    调用一个生成器函数，返回的是一个迭代器对象。
    为什么存在？ 答：当迭代次数很多很多时，可以先用一次值，丢一次，这样可以节约内存资源。
    a,b
    0 1
    1 1
    1 2
    2 3
    3 5
    5 8
    ...
    从上述结果看，对a迭代即可获取斐波那契数列
    """
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


def generator(m):
    f = fibonacci(m)
    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            sys.exit()


def joinStr(x):
    page_str = ""
    for i in range(x):
        ele = '<li><a href=?{}>{}</a></li>'.format(i, i)
        tt = page_str + ele
        yield tt


if __name__ == '__main__':
    # iterator()
    # generator(20)
    p = joinStr(21)
    print(p)
    print(next(p))
    print(next(p))
    print(next(p))
