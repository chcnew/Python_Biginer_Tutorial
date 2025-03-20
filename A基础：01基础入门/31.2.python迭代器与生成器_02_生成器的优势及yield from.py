"""
 * @Description: Python3.8
 * @Author: chc
 * @CreateDate: 2022/3/5
 * @Environment: Anaconda3
"""
import time


def main():
    # 内存爆炸
    # sum__ = sum([i for i in range(100000000000)])
    # 生成器取一个用一个
    # sum__ = sum(i for i in range(100000000000))
    # sum__ = sum(i for i in range(100000))
    # print(sum__)

    # yield from方法
    # def test_yield_from(*iterables):
    #     for i in iterables:
    #         for j in i:
    #             yield j

    # 优雅的改写为
    def test_yield_from(*iterables):
        for i in iterables:
            yield from i

    test = test_yield_from([1, 2, 3, 4])

    print(next(test))
    print(next(test))
    print(next(test))


if __name__ == '__main__':
    start = time.perf_counter()  # 程序运行起始时间
    main()
    print('运行耗时:', time.perf_counter() - start)  # 程序运行结束时间
