# coding: utf-8

# 假设景区有两个窗口，通过系统判断余票有多少再去卖票
# 因为涉及到一张票不可能被两个地方同时使用，所以可以用线程实现
# 假设不设置线程锁 就会出现错乱 因为线程是同时使用资源在运行的


import threading
import time

# 设置线程锁
lock = threading.Lock()
num = 100


def sale(name):
    lock.acquire()  # 获得线程锁
    global num
    if num > 0:
        num = num - 1
        print(name, '卖出1张票，还剩', num, '张。')
    lock.release()  # 释放线程锁


for i in range(num):
    t1 = threading.Thread(target=sale, args=('A窗口',))  # 线程1
    t2 = threading.Thread(target=sale, args=('B窗口',))  # 线程2
    t1.start()
    t2.start()

print('票已经卖完了！')
