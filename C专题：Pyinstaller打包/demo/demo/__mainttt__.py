# _*_coding: utf-8 _*_

"""
功能：
"""
import os
import sys

if getattr(sys, 'frozen ', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print(BASE_DIR)
