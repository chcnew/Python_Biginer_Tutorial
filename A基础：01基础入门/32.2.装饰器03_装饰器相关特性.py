"""
 * @Description: Python3.8
 * @Author: chc
 * @CreateDate: 2022/3/4
 * @Environment: Anaconda3
"""
import functools


def outer(func):
    """装饰器"""

    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)

    return inner


@outer
def login():
    pass


if __name__ == '__main__':
    print(login.__name__)  # inner不加装饰器：@functools.wraps(func)，则结果为inner；反之为login
