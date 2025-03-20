# _*_ coding: utf-8 _*_

"""
功能：
"""
import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from tqdm import tqdm

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def long_running_task(task_id):
    """ 模拟一个长时间运行的任务 """
    time.sleep(3)  # 模拟耗时任务
    return f"{task_id} is T"


def test_long_running_tasks():
    num_tasks = 10  # 任务总数
    tasks = list(range(num_tasks))  # 创建任务列表

    # 创建一个线程池
    with ThreadPoolExecutor(max_workers=2) as executor:
        # 提交任务到线程池
        futures = {executor.submit(long_running_task, task): task for task in tasks}

        # 显示进度条
        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing"):
            result = future.result()  # 获取任务结果
            # 可以在这里做一些断言或处理
            logger.info(f"Task {result} completed.")
