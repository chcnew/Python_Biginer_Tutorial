"""
 * @Description: Python3.8
 * @Author: chc
 * @CreateDate: 2022/3/4
 * @Environment: Anaconda3
"""
import time


def main():
    """
    对象三大基本要素:
        -address(内存地址)
        -type(数据类型)
        -value(值)
    is与==区别：
        比较的要素不同
        == 比较的是值，相同或相等返回True,否则False
        is 比较的是内存地址，相同返回True,否则False
    """

    # ==条件判断 过于简单不说了~~
    # is场景
    # 此类赋值，x，y内存地址相同
    x = y = 123
    z = 456
    print(id(x), ";  ", id(y))
    print(x is y)
    print(y is x)
    print(z is x)
    print(z is y)

    # 此类赋值，p，q内存地址不相同
    p = 111
    q = 222
    # id可以输出内存地址
    print(id(p), ";  ", id(q))
    print(p is q)


if __name__ == '__main__':
    start = time.perf_counter()  # 程序运行起始时间
    main()
    print('运行耗时:', time.perf_counter() - start)  # 程序运行结束时间
