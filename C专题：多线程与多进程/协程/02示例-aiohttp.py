# _*_ coding: utf-8 _*_

"""
功能：推荐版本 aiohttp==3.10.6
"""
# _*_ coding: utf-8 _*_
import asyncio

import aiohttp


async def fetch_status(session: aiohttp.ClientSession, url: str) -> dict:
    print(f'Fetching status for {url}')
    async with session.get(url) as response:  # 异步发起 GET 请求
        status = response.status
        print("Done!")
        return {"status": status, "url": url}


async def main():
    async with aiohttp.ClientSession(trust_env=True) as session:  # 创建异步 HTTP 会话 （python3.12报错但不影响执行）
        baidu_task = asyncio.create_task(fetch_status(session, "https://www.baidu.com"))
        apple_task = asyncio.create_task(fetch_status(session, "https://www.apple.com"))

        baidu_status = await baidu_task
        apple_status = await apple_task

        print(baidu_status)
        print(apple_status)


if __name__ == '__main__':
    asyncio.run(main(), debug=True)
