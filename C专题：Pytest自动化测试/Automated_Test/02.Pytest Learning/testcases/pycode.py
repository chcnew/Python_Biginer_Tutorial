# -*- coding:utf-8 -*-

import concurrent.futures
import sys

import pytest


# 定义一个函数来运行 Pytest 测试用例
def run_tests(test_file, progress_callback):
    result = pytest.main([test_file, '--disable-warnings', '--maxfail=1'])
    # 使用进度回调来更新进度
    progress_callback(test_file, result)


# 进度更新回调函数
def update_progress(test_file, result):
    # 这里我们可以更新进度条或日志，示例中我们只是简单打印
    print(f"Finished running {test_file}. Result code: {result}")


def main(test_files):
    # 创建一个线程池
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 为每个测试文件提交一个任务
        futures = []
        for test_file in test_files:
            future = executor.submit(run_tests, test_file, update_progress)
            futures.append(future)

        # 等待所有线程完成
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  # 获取任务的结果
            except Exception as exc:
                print(f'Generated an exception: {exc}', file=sys.stderr)


if __name__ == '__main__':
    test_files = ['test_file1.py', 'test_file2.py']  # 你可以在这里指定测试文件
    main(test_files)
