"""
 * @Description: Python3.8
 * @Author: chc
 * @CreateDate: 2022/3/4
 * @Environment: Anaconda3
"""


def uppercase_decorator(func):
    def inner(*args, **kwargs):
        s = func()
        make_uppercase = s.upper()  # 小写改大写
        return make_uppercase

    return inner


# @uppercase_decorator
def say_hello():
    return "hello world!"


def main():
    # 实现调用sya_hello函数的时候，再次调用uppercase_decorator函数
    # 此处调用say_hello函数不带括号
    say_hello_new = uppercase_decorator(say_hello)
    print(say_hello_new())


if __name__ == '__main__':
    main()
