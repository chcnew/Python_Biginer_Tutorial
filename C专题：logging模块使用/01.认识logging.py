# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

logging.debug("Debug信息")
logging.info("INFO信息")
logging.warning("WARNING信息")
logging.error("ERROR信息")
logging.critical("CRITICAL信息")

# 从上至下级别依次升高
# 默认日志打印级别：>= warning

"""结果:
WARNING:root:WARNING信息
ERROR:root:ERROR信息
CRITICAL:root:CRITICAL信息
"""
