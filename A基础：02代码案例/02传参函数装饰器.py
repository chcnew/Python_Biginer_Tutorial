# -*- coding: utf-8 -*-

"""
功能：
"""
from functools import wraps


def supdecorator(**params):
    """传参函数装饰器"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("start\n")
            print(f"globals: {globals()}")
            for key, value in params.items():
                globals()[key] = value
            result = func(*args, **kwargs)
            for key, value in params.items():
                globals().pop(key)
            print("\nend")
            print(f"globals: {globals()}")
            return result

        return wrapper

    return decorator


class A:

    def __init__(self):
        self.name = "xxx"
        self.gender = "男"
        self.age = "18"

    @supdecorator(current_status_strvar="xxx001")
    def say_hello(self):
        # print(self.say_hello.current_status_strvar)
        print(current_status_strvar)
        print(self.say_hello.__name__)
        print(self.name)
        print(self.gender)
        print(self.age)


if __name__ == '__main__':
    A().say_hello()
