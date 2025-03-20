# coding: utf-8

from multiprocessing import Process
import time


def run(xname):
    print(xname, '进程执行了！')
    time.sleep(5)


if __name__ == '__main__':
    p1 = Process(target=run, args=('p1',))
    p2 = Process(target=run, args=('p2',))
    p3 = Process(target=run, args=('p3',))
    p4 = Process(target=run, args=('p4',))
    # 相对于我的4核心电脑 肯定是4个进程同时处理 再继续下一轮 每次可以执行最多四个
    p5 = Process(target=run, args=('p5',))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    # 加入主进程
    p1.join()
    p2.join()
    p3.join()
