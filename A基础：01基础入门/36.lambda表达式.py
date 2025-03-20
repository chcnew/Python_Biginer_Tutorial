"""
 * @Description: Python3.8
 * @Author: chc
 * @CreateDate: 2022/3/5
 * @Environment: Anaconda3
"""
import random
import time


def main():
    # 简单用法
    lam = lambda x, y=1, z=2: x + y * z
    print(lam(1, 2, 3))

    # if语句：区分奇数偶数
    get_even_odd = lambda x: "偶数" if x % 2 == 0 else "奇数"
    print(get_even_odd(12))

    # 指向函数
    lam_ran = lambda: random.random()
    print(lam_ran())

    # 配合map函数使用
    # map函数：可以将可迭代对象中的每一个元素作为参数代入另外的函数
    def fun(x):
        return x ** 2

    m1 = map(fun, [1, 2, 3, 4])
    print(list(m1))

    # lambda实现
    m2 = map(lambda x: x ** 2, [1, 2, 3, 4])
    print(list(m2))


if __name__ == '__main__':
    start = time.perf_counter()  # 程序运行起始时间
    main()
    print('运行耗时:', time.perf_counter() - start)  # 程序运行结束时间
