# _*_ coding: utf-8 _*_

"""
功能：
"""
import asyncio
from asyncio import Task

import requests
from requests import Response


async def fetch_status(url: str) -> dict:
    print(f'Fetching status for {url}')
    response: Response = await asyncio.to_thread(requests.get, url)
    print("Done!")
    return {"status": response.status_code, "url": url}


async def main():
    baidu_task: Task = asyncio.create_task(fetch_status("https://www.baidu.com"))
    apple_task: Task = asyncio.create_task(fetch_status("https://www.apple.com"))

    baidu_status = await baidu_task
    apple_status = await apple_task

    print(baidu_status)
    print(apple_status)


if __name__ == '__main__':
    asyncio.run(main(), debug=True)
