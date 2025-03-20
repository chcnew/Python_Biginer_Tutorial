# _*_encoding: utf-8 _*_

"""
ss = psutil.process_iter()  # 获取所有进程，返回迭代器
ss = psutil.pids()  # 获取所有进程，返回列表
psutil.pid_exists(pid)  # 判断pid的进程是否存在
s = psutil.Process()  # 获取当前进程，可以加参数，指定进程pid
s.pid  # 进程pid
s.name()  # 进程名
s.nice()  # 不加参数，输出进程优先级，加参数，设定进程优先级
s.status()  # 进程当前状态
s.is_running()  # 进程是否运行，返回True或False
s.parent()  # 当前进程父进程
s.children()  # 当前进程子进程
s.ppid()  # 父进程pid
s.cwd()  # 进程工作路径
s.create_time()  # 进程创建时间
s.num_threads()  # 进程使用线程数
s.cpu_percent()  # 当前进程cpu利用率，返回一个浮点数
"""
import os
import time
from multiprocessing import Process
import psutil


def fun(tx1):
    pro_now = psutil.Process()
    pid = pro_now.pid
    i = 0
    while 1:
        print(pid, tx1, i)
        print("优先级：{}".format(pro_now.nice()))
        i += 1
        time.sleep(1)


# 改变进程优先级
def change_fun(o_pid):
    processs = psutil.process_iter()
    # 设置高优先级
    for pro in processs:
        if pro.pid in o_pid:
            print('改变之前：', pro.pid, pro.nice())
            # pro.nice(psutil.HIGH_PRIORITY_CLASS)
            # linux下进程调度优先级是从-20到19，一共40个级别，数字越大，表示进程的优先级越低。默认进程优先级是0。
            os.system("renice -n 2 -p {}".format(pro.pid))
            print('改变之后：', pro.pid, pro.nice())

        # 参数选择:
        # psutil.NORMAL_PRIORITY_CLASS,  #  -> 正常优先级
        # psutil.BELOW_NORMAL_PRIORITY_CLASS,  #  ->低于正常优先级
        # psutil.ABOVE_NORMAL_PRIORITY_CLASS,  #  ->高于正常优先级
        # psutil.HIGH_PRIORITY_CLASS,  #  ->高优先级
        # psutil.REALTIME_PRIORITY_CLASS  #  ->实时优先级


if __name__ == '__main__':
    # 和多线程第一种方法很类似
    names = [['one', '周'], ['two', '张'], ['three', '刘'], ['four', '宋'],
             ['five', '赵'], ['six', '钱'], ['seven', '孙'], ['eight', '李']]
    # 创建8个进程
    for name in names:
        Process(target=fun, name=name[0], args=(name[1],)).start()  # 使用args进行传参，需要逗号

    # 获取当前进程
    ss = psutil.Process()
    print("主pid:", ss.pid)
    # 获取子进程pid
    childs = ss.children()
    child_pids = [child.pid for child in childs]
    change_fun(child_pids)
