# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

fmt = "%(name)s-->%(message)s-->%(asctime)s"  # 设置显示格式: 日志器名称-->信息-->时间
logging.basicConfig(level="DEBUG", format=fmt)  # 定义显示配置

logging.debug("Debug信息")
logging.info("INFO信息")
logging.warning("WARNING信息")
logging.error("ERROR信息")
logging.critical("CRITICAL信息")

"""结果:
root-->Debug信息-->2022-10-13 15:59:54,001
root-->INFO信息-->2022-10-13 15:59:54,002
root-->WARNING信息-->2022-10-13 15:59:54,002
root-->ERROR信息-->2022-10-13 15:59:54,002
root-->CRITICAL信息-->2022-10-13 15:59:54,002
"""
