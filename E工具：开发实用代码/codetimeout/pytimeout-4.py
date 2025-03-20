# _*_ coding: utf-8 _*_

"""
功能：
"""

import subprocess

proc = subprocess.Popen("python -B -c \"import time; time.sleep(10)\"; print(ux)", shell=True)
try:
    proc.wait(timeout=3)
except subprocess.TimeoutExpired as err:
    print(err)
