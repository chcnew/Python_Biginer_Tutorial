# coding: utf-8

# 线程锁锁的是代码 让资源只能被一个线程占用
import threading

lock = threading.Lock()  # 相当于对象实例化 互斥锁

num = 100


def run(somex):
    lock.acquire()  # 开始设置线程锁代码段
    global num  # 设置为全局变量 就是函数体外的变量num=100
    num = num - 1
    print('线程', somex, '执行了，现在num的值为:', num)
    lock.release()  # 释放线程锁


# 启动100个线程
for i in range(100):
    t = threading.Thread(target=run, args=(i + 1,))
    t.start()

# 关于python本身 全局解释器锁(GIL) --> 起到的作用更多表现为负面的 python的缺点！
# 其本意目的是为了保护数据的安全性，但却弊大于利。
# 造成当pc的为多核心时，每次还是只能运行一个线程，造成了cpu资源浪费。
# 不管cpu核心数是多少，都保证Python同一时间点只能执行一个线程
# python缺点

# 如何解决？
# 引入多进程 GIL只能针对线程 无法限制进程 即可解决。
