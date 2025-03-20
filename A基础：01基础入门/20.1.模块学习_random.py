"""
 * @Description: Python3.8
 * @Author: chc
 * @CreateDate: 2022/3/4
 * @Environment: Anaconda3
"""

import random
import time


def main():
    # 生成0~1之间的随机数
    print(random.random())
    # 生成大于等于0，且小于10，步长为1的随机整数
    print(random.randrange(10))
    # 生成大于等于0，且小于10，步长为1的随机整数
    print(random.randrange(5, 10, 2))


if __name__ == '__main__':
    start = time.perf_counter()  # 程序运行起始时间
    main()
    print('运行耗时:', time.perf_counter() - start)  # 程序运行结束时间
