"""
 * @Description: Python3.8
 * @Author: chc
 * @CreateDate: 2022/3/4
 * @Environment: Anaconda3
"""
import time


def uppercase_decorator(func):
    def inner(*args, **kwargs):
        s = func()
        make_uppercase = s.upper()  # 小写改大写
        return make_uppercase

    return inner  # 不带括号


def bracket_decorator(func):
    def inner(*args, **kwargs):
        s = func()
        make_bracket = "[" + s + "X" + "]"
        return make_bracket

    return inner  # 不带括号


@uppercase_decorator
@bracket_decorator
def say_hello():
    return "hello world!"


def main():
    # 使用装饰器执行
    print(say_hello())


if __name__ == '__main__':
    start = time.perf_counter()  # 程序运行起始时间
    main()
    print('运行耗时:', time.perf_counter() - start)  # 程序运行结束时间
