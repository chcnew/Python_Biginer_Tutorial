# _*_ coding: utf-8 _*_

"""
功能：测试self到底是谁
每次进入父类，其实self对象还是自己，肯定先从自己去找
"""


class Base(object):
    xxx = "bbb"

    def func1(self):
        self.func2()
        print(self.xxx)

    def func2(self):
        print("base.func2")


class Foo(Base):
    xxx = "fff"

    def func2(self):
        print("foo.func2")
        super().func2()


if __name__ == '__main__':
    foo = Foo()
    foo.func1()
