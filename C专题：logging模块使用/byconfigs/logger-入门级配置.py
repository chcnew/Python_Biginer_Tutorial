import logging.config
# from concurrent_log_handler import ConcurrentRotatingFileHandler

log_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': logging.DEBUG,
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'app.log',
            'formatter': 'standard',
            'level': logging.DEBUG,
            'encoding': 'utf-8'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': logging.DEBUG,
            'propagate': True,
        },
    }
}

logging.config.dictConfig(log_config)

logger = logging.getLogger(__name__)

logger.debug('这是一个调试消息')
logger.info('这是一个信息消息')
logger.warning('这是一个警告消息')
logger.error('这是一个错误消息')
logger.critical('这是一个致命错误消息')
