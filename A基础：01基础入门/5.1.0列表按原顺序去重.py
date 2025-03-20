"""
 * @Description: Python3.8
 * @Author: chc
 * @CreateDate: 2022/3/4
 * @Environment: Anaconda3
"""
import time


def main():
    # 去重且保持顺序不变
    a = [1, 2, "test", 1, 1, 2]
    b = list(set(a))
    b.sort(key=a.index)
    print(b)


if __name__ == '__main__':
    start = time.perf_counter()  # 程序运行起始时间
    main()
    print('运行耗时:', time.perf_counter() - start)  # 程序运行结束时间
