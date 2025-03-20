# _*_ coding: utf-8 _*_

"""
功能：
"""

import threading
import time


def target_function(stop_flag):
    while not stop_flag.is_set():
        print("Thread is running...")
        time.sleep(1)


# 创建线程停止标志
stop_flag = threading.Event()

# 创建线程，并传递停止标志
thread = threading.Thread(target=target_function, args=(stop_flag,))

# 启动线程
thread.start()

# 等待一段时间
time.sleep(5)

# 设置停止标志，线程会在检测到标志后自行退出
stop_flag.set()

# 等待线程结束
thread.join()
