# _*_ coding: utf-8 _*_

"""
功能：
"""
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import requests

from logger import logger_task

SSS = """
1
2
3
"""

# 示例列表
data_list = SSS.strip().splitlines()
logger_task.info("len(data_list)={}".format(len(data_list)))

# 接口 URL
api_url = "http://bsp.vivo.xyz:8081/handle_docu_number"
wait_time = 3


# 定义一个函数，用于调用接口
def call_api(data):
    global wait_time

    try:
        # response = requests.post(api_url, json={"docu_number": data}, timeout=10)  # 发送 POST 请求
        response = requests.get("https://www.baidu.com/", timeout=10)  # 发送 POST 请求
        if response.status_code == 200:
            logger_task.info(f"Success: {data} -> {response.json()}")
        else:
            logger_task.info(f"Failed: {data} -> Status Code: {response.status_code}")
        return response.json()  # 返回响应
    except requests.RequestException as e:
        logger_task.info(f"Error: {data} -> {e}")
        return None
    finally:
        total_seconds = wait_time * 60  # 转换为秒
        logger_task.info(f"Waiting for {wait_time} minutes before the next request for {data}...")

        for remaining_seconds in range(int(total_seconds), 0, -1):
            # 使用 ANSI 转义序列覆盖上一行的输出
            sys.stdout.write(f"\rTime remaining: {remaining_seconds // 60} min {remaining_seconds % 60} sec")
            sys.stdout.flush()
            time.sleep(1)


# 定义线程池并处理任务
def process_with_thread_pool(data_list, max_workers=3):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(call_api, data_list))
    return results


# 调用线程池处理
if __name__ == "__main__":
    results = process_with_thread_pool(data_list)
    logger_task.info("All tasks completed. Results:")
    logger_task.info(f"results: {results}")
