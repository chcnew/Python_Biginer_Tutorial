# _*_ coding: utf-8 _*_

"""
功能：
"""
from celery import Celery

app = Celery('demo')  # 创建 Celery 实例
app.config_from_object('wedo.config')
