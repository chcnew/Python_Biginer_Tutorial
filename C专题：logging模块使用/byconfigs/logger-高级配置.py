# _*_ coding: utf-8 _*_

"""
功能：

作为 Handler 基类的补充，提供了很多有用的子类：
    StreamHandler 实例发送消息到流（类似文件对象）。
    FileHandler 实例将消息发送到硬盘文件。
    BaseRotatingHandler 是轮换日志文件的处理器的基类。它并不应该直接实例化。而应该使用 RotatingFileHandler 或 TimedRotatingFileHandler 代替它。
    RotatingFileHandler 实例将消息发送到硬盘文件，支持最大日志文件大小和日志文件轮换。
    TimedRotatingFileHandler 实例将消息发送到硬盘文件，以特定的时间间隔轮换日志文件。
    SocketHandler 实例将消息发送到 TCP/IP 套接字。从 3.4 开始，也支持 Unix 域套接字。
    DatagramHandler 实例将消息发送到 UDP 套接字。从 3.4 开始，也支持 Unix 域套接字。
    SMTPHandler 实例将消息发送到指定的电子邮件地址。
    SysLogHandler 实例将消息发送到 Unix syslog 守护程序，可能在远程计算机上。
    NTEventLogHandler 实例将消息发送到 Windows NT/2000/XP 事件日志。
    MemoryHandler 实例将消息发送到内存中的缓冲区，只要满足特定条件，缓冲区就会刷新。
    HTTPHandler 实例使用 GET 或 POST 方法将消息发送到 HTTP 服务器。
    WatchedFileHandler 实例会监视他们要写入日志的文件。如果文件发生更改，则会关闭该文件并使用文件名重新打开。此处理器仅在类 Unix 系统上有用； Windows 不支持依赖的基础机制。
    QueueHandler 实例将消息发送到队列，例如在 queue 或 multiprocessing 模块中实现的队列。
    NullHandler 实例不对错误消息执行任何操作。 如果库开发者希望使用日志记录，但又希望避免出现“找不到日志记录器 XXX 的处理器”消息则可以使用它们。 更多信息请参阅 为库配置日志。
"""
import datetime
import logging.config
import os.path
import threading
import time
from logging.handlers import TimedRotatingFileHandler

from django.conf import settings

# from concurrent_log_handler import ConcurrentRotatingFileHandler, ConcurrentTimedRotatingFileHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_Stdy02_EMS.settings")
log_dir = os.path.join(settings.BASE_DIR, "logs")
# log_dir = r'F:\My_Study\1.Python_learning\8.Django_Learning\Django_Stdy02_EMS\logs'
today = datetime.datetime.now().strftime('%Y%m%d')


class ThreadNameFilter(logging.Filter):
    def __init__(self, thread_name, name=''):
        super().__init__(name)
        self.thread_name = thread_name

    def filter(self, record):
        # 仅当线程名称匹配时记录日志
        return threading.current_thread().name == self.thread_name


class CusTimedRotatingFileHandler(TimedRotatingFileHandler):
    """多进程使用优化，当然也可以考虑第三方模块：pip3 install concurrent_log_handler"""

    def doRollover(self):
        """
        do a rollover; in this case, a date/time stamp is appended to the filename
        when the rollover happens.  However, you want the file to be named for the
        start of the interval, not the current time.  If there is a backup count,
        then we have to get a list of matching filenames, sort them and remove
        the one with the oldest suffix.
        """
        if self.stream:
            self.stream.close()
            self.stream = None
        # get the time that this sequence started at and make it a TimeTuple
        currentTime = int(time.time())
        dstNow = time.localtime(currentTime)[-1]
        t = self.rolloverAt - self.interval
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
            dstThen = timeTuple[-1]
            if dstNow != dstThen:
                if dstNow:
                    addend = 3600
                else:
                    addend = -3600
                timeTuple = time.localtime(t + addend)
        dfn = self.rotation_filename(self.baseFilename + "." +
                                     time.strftime(self.suffix, timeTuple))
        # if os.path.exists(dfn):
        #     os.remove(dfn)
        # self.rotate(self.baseFilename, dfn)
        if not os.path.exists(dfn):
            self.rotate(self.baseFilename, dfn)

        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                os.remove(s)
        if not self.delay:
            self.stream = self._open()
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval
        # If DST changes and midnight or weekly rollover, adjust for this.
        if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:  # DST kicks in before next rollover, so we need to deduct an hour
                    addend = -3600
                else:  # DST bows out before next rollover, so we need to add an hour
                    addend = 3600
                newRolloverAt += addend
        self.rolloverAt = newRolloverAt


def get_rotating_file_handler(number):
    handler = {
        "class": "logging.handlers.RotatingFileHandler",
        "formatter": "detailed",
        "filename": os.path.join(log_dir, f'RotatingFileHandler{number}-{today}.log'),
        "maxBytes": 10 * 1024 * 1204,  # 最大10M
        "backupCount": 7,
        "encoding": "utf-8"
    }
    return handler


def get_timed_rotating_file_handler(number):
    handler = {
        "class": "logging.handlers.TimedRotatingFileHandler",
        "formatter": "detailed",
        "filename": os.path.join(log_dir, f'timedRotatingFileHandler{number}-{today}.log'),
        "when": "midnight",
        "interval": 1,
        "backupCount": 7,
        "encoding": "utf-8"
    }
    return handler


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
            'formatter': 'detailed',
            'level': logging.DEBUG
        },
        "timedRotatingFileHandler1": get_rotating_file_handler(1),
        "timedRotatingFileHandler2": get_timed_rotating_file_handler(2),
        "timedRotatingFileHandler3": get_timed_rotating_file_handler(3),
        "concurrentRotatingFileHandler": {
            "class": "concurrent_log_handler.ConcurrentRotatingFileHandler",
            "formatter": "detailed",
            "filename": os.path.join(log_dir, f'concurrentRotatingFileHandler-{today}.log'),
            "maxBytes": 10485760 // 10,
            "backupCount": 7,
            "encoding": "utf-8"
        }

    },
    'loggers': {
        'logger1': {
            'handlers': ['console', 'timedRotatingFileHandler1'],
            'level': logging.DEBUG,
            'propagate': True,
        },
        'logger2': {
            'handlers': ['console', 'timedRotatingFileHandler2'],
            'level': logging.DEBUG,
            'propagate': True,
        },
        'logger3': {
            'handlers': ['console', 'timedRotatingFileHandler3'],
            'level': logging.DEBUG,
            'propagate': True,
        },
        'logger_error': {
            'handlers': ['console', 'concurrentRotatingFileHandler'],
            'level': logging.ERROR,
            'propagate': False,
        },
        'logger_runtime': {
            'handlers': ['console', 'concurrentRotatingFileHandler'],
            'level': logging.ERROR,
            'propagate': False,
        },
    }
}


def remove_handler(logger, name=''):
    """删除handler"""

    def rmh(handler):
        logger.removeHandler(handler)
        if not hasattr(handler, "close"):
            handler.close()

    for handler in logger.handlers:
        if name and handler.name == name:
            rmh(handler)
            break

        rmh(handler)


def update_log_file_path(new_path, handler):
    """
    函数用于更新 FileHandler 的路径

    :param new_path: 新的log文件路径
    :param handler: 处理器对象
    :return:
    """
    handler.baseFilename = new_path
    handler.stream.close()  # 关闭旧的文件
    handler.stream = open(new_path, 'a')  # 打开新的文件


def logger_runtime_init(new_path, thread_name):
    """
    运行时修改日志路径，同时添加过滤器

    :param new_path:
    :param thread_name:
    :return:
    """
    for handler in logger_runtime.handlers:
        # 添加之前先移除或者判断是否存在
        for flt in handler.filters:
            if flt.name == "my_thread_name_filter":
                handler.removeFilter(flt)
                break
        if handler.name == 'concurrentRotatingFileHandler':
            update_log_file_path(new_path, handler)
            thread_name_filter = ThreadNameFilter(thread_name, "my_thread_name_filter")
            handler.addFilter(thread_name_filter)


def logger_runtime_deinit():
    """移除所有logger_runtime的处理器"""
    remove_handler(logger_runtime)


logging.config.dictConfig(log_config)
logger1 = logging.getLogger('logger1')
logger2 = logging.getLogger('logger2')
logger3 = logging.getLogger('logger3')
logger_error = logging.getLogger('logger_error')
logger_runtime = logging.getLogger('logger_runtime')

if __name__ == '__main__':
    logger1.debug('这是一个调试消息')
    logger2.info('这是一个信息消息')
    logger3.warning('这是一个警告消息')
    logger_error.error('这是一个错误消息')
    logger1.critical('这是一个致命错误消息')

    try:
        1 / 0
    except ZeroDivisionError as e:
        logger_error.error('捕捉到异常', exc_info=True)
