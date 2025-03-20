# _*_ coding: utf-8 _*_

"""
功能：递归杀死子进程
"""
import time

import psutil


def kill_process_tree(pid):
    """ChatGPT"""
    print("递归杀死父进程及其全部子进程")
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
        print(f"父进程：{parent.pid}")
        print(f"父进程状态：{parent.status()}")
    except Exception as err:
        print(f"Error terminating process tree: {err}")


def kill_process_children(pid):
    """杀死子进程，不杀死父进程"""
    print("递归只杀死子进程，父进程不杀死")
    try:
        parent = psutil.Process(pid)
        children = parent.children(recursive=True)
        for idx, child in enumerate(children):
            print(f"child-{idx}: {child.pid}")
            child.kill()  # 强制杀死未终止的子进程
        print(f"父进程：{parent.pid}")
        print(f"父进程状态：{parent.status()}")
    except Exception as err:
        print(f"Error terminating process tree: {err}")


def print_info(num):
    while True:
        print(num)
        time.sleep(1)


if __name__ == '__main__':
    # kill_process_tree(3552)
    # kill_process_children(9460)

    parent = psutil.Process(6412)
    print(parent.status())
