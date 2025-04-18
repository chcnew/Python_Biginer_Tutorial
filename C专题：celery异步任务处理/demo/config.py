# _*_ coding: utf-8 _*_

"""
功能：
"""
BROKER_URL = 'redis://10.8.238.2:6379/0'  # Broker配置，使用Redis作为消息中间件
CELERY_RESULT_BACKEND = 'redis://10.8.238.2:6379/0'  # BACKEND配置，这里使用redis
CELERY_RESULT_SERIALIZER = 'json'  # 结果序列化方案
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  # 任务过期时间
CELERY_TIMEZONE = 'Asia/Shanghai'  # 时区配置
CELERY_IMPORTS = (  # 指定导入的任务模块,可以指定多个
    'wedo.tasks',
    'wedo.period_task'
)
