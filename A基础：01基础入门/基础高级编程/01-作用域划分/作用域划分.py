# _*_ coding: utf-8 _*_

"""
功能：python代码作用域划分

内建作用域：Built-in  -> builtins.py 定义的函数等
全局作用域：Global
函数作用域：Enclosing  -> 闭包
局部作用域：Local
"""

a = 0  # 全局作用域变量
var4 = 100


def func1():
    b = 1  # 函数作用域变量

    def func2():
        print(f"func2-b: {b}")
        print(f"func2-c: {c}")

        for i in range(5):
            if globals().get("var4"):
                print(f"globals-var4: {var4}")
            globals()[f"var{i}"] = i  # 动态创建全局作用域变量
        print(f"func2-var4: {var4}")

    print(f"func1-b: {b}")

    c = 3  # 函数作用域变量
    print(f"func1-c: {c}")

    return func2


if __name__ == '__main__':
    func = func1()
    func()
