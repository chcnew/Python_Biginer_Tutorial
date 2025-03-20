# _*_ coding: utf-8 _*_

"""
功能：
"""
import logging
import multiprocessing


def get_logger(name):
    logger = logging.Logger(name)
    logger.setLevel("DEBUG")
    ch = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s.%(msecs).03d | "
                                  "[%(filename)s | %(lineno)s | %(funcName)s] "
                                  "[%(levelname)s] | "
                                  "%(message)s")
    ch.setFormatter(formatter)
    ch.setLevel("DEBUG")
    logger.addHandler(ch)
    return logger


class Runner:
    def __init__(self):
        self.var = "TTT"
        self.logger = get_logger("B")

    def run(self):
        self.logger.info(self.var)


def main_process():
    runner = Runner()
    runner.logger.info("xxx")
    runner.run()


if __name__ == '__main__':
    # ---------错误示例---------
    # logger = get_logger("A")
    # logger.info("Start...")
    # runner = Runner()
    # p = multiprocessing.Process(target=runner.run)
    # p.start()
    # p.join()
    # ---------正确示例---------
    logger = get_logger("A")
    logger.info("Start...")
    p = multiprocessing.Process(target=main_process)
    p.start()
    p.join()
