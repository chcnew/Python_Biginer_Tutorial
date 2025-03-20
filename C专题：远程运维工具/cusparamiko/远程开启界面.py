# -*- coding: utf-8 -*-

"""
功能：
"""
import win32api

windows_python = "python.exe"
command_params = "xxx"
ret = win32api.ShellExecute(
    0, 'open', windows_python, command_params, '', 3)
logger.info(f"windows_python: {windows_python}")
logger.info(f"command_params: {command_params}")
if ret > 32:
    logger.info(f"ret: {ret}, 【正常值：> 32】")
else:
    logger.warning(f"ret: {ret}, 【异常值：<= 32】")
