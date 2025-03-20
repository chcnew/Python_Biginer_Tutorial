# _*_ coding: utf-8 _*_

"""
功能：
"""

import os
import threading
import time


def exec_shell(cmd_str, timeout=8):
    def run_shell_func(sh):
        ret = os.system(sh)
        if ret != 0:
            print("ERROR")
        else:
            print("SUCCESS")

    start_time = time.time()
    t = threading.Thread(target=run_shell_func, args=(cmd_str,), daemon=True)
    t.start()
    while True:
        now = time.time()
        if now - start_time >= timeout:
            if not t.is_alive():
                return 'exec_shell_complete'
            else:
                return 'exec_shell_timeout'
        if not t.is_alive():
            return 'exec_shell_complete'
        time.sleep(1)


res = exec_shell("python -B -c \"import time; time.sleep(3)\"; print(ux)")
print(res)
