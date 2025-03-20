# _*_ coding: utf-8 _*_

"""
功能：递归杀死子进程
"""
import multiprocessing
import os
import time

import psutil


def kill_process_tree_cf(pid, logger, kill_parent=True):
    """递归终止进程及其子进程"""
    if not pid:
        return

    try:
        parent = psutil.Process(pid)
    except psutil.NoSuchProcess as err:
        logger.warning(err)
    except Exception as err:
        logger.error(err, exc_info=True)
    else:
        logger.info("*" * 34 + f"kill_process_and_child, kill_parent={kill_parent}" + "*" * 34)
        logger.info(f"parent pid={parent.pid}")
        children = parent.children(recursive=True)
        for child in children:
            try:
                child.kill()  # 强制杀死子进程
            except Exception as err:
                logger.warning(
                    f"Error terminating child process, pid={child.pid}, ErrorMessage: {err}")
            else:
                logger.info(
                    f"Success terminating child process, pid={child.pid}")
        # 清理父进程开关打开
        if kill_parent:
            try:
                parent.kill()  # 强制杀死父进程
            except Exception as err:
                logger.warning(
                    f"Error terminating parent process, pid={parent.pid}, ErrorMessage: {err}")
            else:
                logger.info(
                    f"Success terminating parent process, pid={parent.pid}")
        logger.info("*" * 108)


def kill_process_tree(pid):
    """ChatGPT"""
    try:
        parent = psutil.Process(pid)
        children = parent.children(recursive=True)
        for child in children:
            child.terminate()  # 终止子进程
        _, alive = psutil.wait_procs(children, timeout=5)
        for child in alive:
            child.kill()  # 强制杀死未终止的子进程
        parent.terminate()  # 终止父进程
        parent.wait(timeout=5)  # 等待父进程终止
    except Exception as e:
        print(f"Error terminating process tree: {e}")


def kill_process_children(pid):
    """杀死子进程，不杀死父进程"""
    try:
        parent = psutil.Process(pid)
    except Exception as err:
        raise err
    children = parent.children(recursive=True)
    for child in children:
        try:
            child.kill()  # 强制杀死未终止的子进程
        except Exception as err:
            print(f"Error terminating process tree: {err}")
        else:
            print(f"Has been killed child process pid: {child.pid}")


def print_info(num):
    print(f"print_info: {os.getpid()}")
    while True:
        print(num)
        time.sleep(1)


def mkchild():
    print(f"mkchild: {os.getpid()}")
    ppp = multiprocessing.Process(target=print_info, args=(9,))
    ppp.start()
    for i in range(3):
        locals()[f"p{i}"] = multiprocessing.Process(target=print_info, args=(i,))
        locals()[f"p{i}"].start()
        if i == 2:
            locals()[f"p{i}"].join()


if __name__ == '__main__':
    # 示例：获取当前进程的PID并杀死所有子进程
    # current_pid = os.getpid()
    # kill_process_tree(current_pid)
    print(f"__main__: {os.getpid()}")
    p = multiprocessing.Process(target=mkchild)
    p.start()
    p.join()
    print("子进程已全部被关闭....")
    print("finished!")
    time.sleep(20)
