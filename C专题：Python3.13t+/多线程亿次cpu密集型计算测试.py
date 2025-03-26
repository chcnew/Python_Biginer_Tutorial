# _*_ coding: utf-8 _*_

"""
当前版本：3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)]

当前GIL禁用状态：0
CPU 密集型任务：
    单线程耗时: 5.36 秒
    多线程耗时: 5.43 秒
    多进程耗时: 2.05 秒

当前GIL禁用状态：1 -- 禁用gil之后，单线程模式反而变慢；但多线程超级快
CPU 密集型任务：
    单线程耗时: 6.69 秒
    多线程耗时: 1.75 秒
    多进程耗时: 2.51 秒
"""

import multiprocessing
import sys
import sysconfig
import threading
import time

GIL_STATUS = sysconfig.get_config_var('Py_GIL_DISABLED')

NUMBER = 100_000_000
GAPS = 250_000
LST = []
for i in range(int(NUMBER / GAPS)):
    if i == 0:
        LST.append((1, GAPS))
    else:
        LST.append((GAPS * i, GAPS * (i + 1)))


# 素数判断函数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 计算素数函数
def calculate_primes(start, end):
    primes = [n for n in range(start, end) if is_prime(n)]
    return primes


# 单线程
def single_thread_task():
    calculate_primes(1, NUMBER)


# 多线程
def multi_thread_task():
    threads = []
    for start, end in LST:
        thread = threading.Thread(target=calculate_primes, args=(start, end))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


# 多进程
def multi_process_task():
    with multiprocessing.Pool(4) as pool:
        pool.starmap(calculate_primes, LST)


if __name__ == "__main__":
    print(f"当前版本：{sys.version}")
    print(f"当前GIL禁用状态：{GIL_STATUS}")

    print("CPU 密集型任务：")

    # 单线程测试
    # start_time = time.time()
    # single_thread_task()
    # print(f"\t单线程耗时: {time.time() - start_time:.2f} 秒")

    # 多线程测试
    start_time = time.time()
    multi_thread_task()
    print(f"\t多线程耗时: {time.time() - start_time:.2f} 秒")

    # 多进程测试
    # start_time = time.time()
    # multi_process_task()
    # print(f"\t多进程耗时: {time.time() - start_time:.2f} 秒")
