# _*_ coding: utf-8 _*_

"""
功能：
"""
# _*_ coding: utf-8 _*_


import logging
import os
import sys
from concurrent_log_handler import ConcurrentRotatingFileHandler


def get_logger(log_path="./", file_name="", fmt=None, console_display=True, debug_switch=False):
    """
    获取日志记录器

    :param log_path: 日志文件保存路径
    :param file_name: 日志文件名
    :param fmt: 自定义日志打印格式
    :param console_display: 是否在控制台打印
    :param debug_switch: debug日志显示开关
    :return:
    """
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    log_file = os.path.join(log_path, file_name)
    logger = logging.getLogger(log_file)
    if logger.handlers:
        return logger

    # 10-DEBUG, 20-INFO
    log_level = 10
    logger.setLevel(log_level)
    default_fmt = "%(asctime)s.%(msecs).03d | " \
                  "%(filename)s | %(lineno)s | %(funcName)s " \
                  "[%(levelname)s] " \
                  "%(message)s"
    if fmt is not None:
        default_fmt = fmt
    formatter = logging.Formatter(default_fmt, "%Y-%m-%d %H:%M:%S")

    # 日添加输出到志文件的handler
    r_handler = ConcurrentRotatingFileHandler(
        filename=log_file,
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8"
    )

    r_handler.setFormatter(formatter)
    if debug_switch:
        r_handler.setLevel(log_level)
    else:
        r_handler.setLevel(20)
    logger.addHandler(r_handler)
    # 添加在终端打印日志的handler
    if console_display:
        console = logging.StreamHandler(sys.stdout)
        console.setFormatter(formatter)
        console.setLevel(10)
        logger.addHandler(console)
    return logger


logger_task = get_logger(file_name="loggerTask.log")
