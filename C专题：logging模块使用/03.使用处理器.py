# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

# 1.创建日志器对象
logger = logging.getLogger(name="MyLogger")
logger.setLevel("DEBUG")

# 2.创建各种处理器对象
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename="./log.txt", mode="a", encoding="utf-8")

# 3.设置等级
console_handler.setLevel("DEBUG")
file_handler.setLevel("WARNING")

# 5.设置格式
console_fmt = logging.Formatter(fmt="%(name)s --> %(message)s --> %(asctime)s")
file_fmt = logging.Formatter(fmt="%(name)s --> %(message)s --> %(lineno)s --> %(asctime)s")
console_handler.setFormatter(console_fmt)
file_handler.setFormatter(file_fmt)

# 6.日志器添加控制台处理器
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 7.日志控制台打印,注意这里用的是创建的日志器对象
logger.debug("Debug信息")
logger.info("INFO信息")
logger.warning("WARNING信息")
logger.error("ERROR信息")
logger.critical("CRITICAL信息")
