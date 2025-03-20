# _*_ coding: utf-8 _*_

"""
功能：
"""
import datetime
import logging.config
import os.path

from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_Stdy02_EMS.settings")
log_dir = os.path.join(settings.BASE_DIR, "logs")
today = datetime.datetime.now().strftime('%Y%m%d')

log_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detailed': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s:%(lineno)d',
        },
        'simple': {
            'format': '%(asctime)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': logging.DEBUG
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(log_dir, f'app01-{today}.log'),
            'formatter': 'detailed',
            'level': logging.DEBUG,
            'encoding': 'utf-8'
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(log_dir, f'app01-errors-{today}.log'),
            'formatter': 'detailed',
            'level': logging.ERROR,
            'encoding': 'utf-8'
        },
        "timedRotatingFileHandler": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "detailed",
            "filename": os.path.join(log_dir, f'app01-timedRotatingFileHandler-{today}.log'),
            "when": "midnight",
            "interval": 1,
            "backupCount": 7
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'timedRotatingFileHandler'],
            'level': logging.DEBUG,
            'propagate': True,
        },
        'error_logger': {
            'handlers': ['error_file'],
            'level': logging.ERROR,
            'propagate': False,
        },
    }
}

logging.config.dictConfig(log_config)
logger = logging.getLogger()
error_logger = logging.getLogger('error_logger')

if __name__ == '__main__':
    logger.debug('这是一个调试消息')
    logger.info('这是一个信息消息')
    logger.warning('这是一个警告消息')
    logger.error('这是一个错误消息')
    logger.critical('这是一个致命错误消息')

    try:
        1 / 0
    except ZeroDivisionError as e:
        error_logger.error('捕捉到异常', exc_info=True)
