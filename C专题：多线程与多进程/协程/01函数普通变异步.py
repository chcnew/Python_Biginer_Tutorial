# _*_ coding: utf-8 _*_

"""
功能：小试牛刀
     写一个异步函数判断网站是否子在线（使用协程）
"""
import asyncio

import requests


async def get_status(url):
    response = await asyncio.to_thread(requests.get, url)
    return response.status_code


async def main():
    urls = [
        'https://www.cnn.com',
        'https://www.baidu.com',
        'https://www.python.org'
    ]
    tasks = [asyncio.create_task(get_status(url)) for url in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(results)


if __name__ == '__main__':
    asyncio.run(main())
