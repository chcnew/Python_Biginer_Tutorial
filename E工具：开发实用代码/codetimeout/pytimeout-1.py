# _*_ coding: utf-8 _*_

"""
功能：
"""

import time

import func_timeout


def main_process(command):
    print(command)
    time.sleep(10)  # 模拟一个耗时10秒的函数


def retn_otime_function(otime):
    @func_timeout.func_set_timeout(otime)  # 设置超时时间为5秒
    def long_running_function(main_process, command):
        main_process(command)

    return long_running_function


if __name__ == '__main__':
    print("0000")
    result_func = retn_otime_function(3)
    try:
        result_func(main_process, "xxxx")
    except func_timeout.exceptions.FunctionTimedOut as err:
        print(str(err).strip())
    print("1111")
