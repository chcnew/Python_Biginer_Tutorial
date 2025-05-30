import asyncio

import aiohttp


async def get_status(session, url):
    async with session.get(url, timeout=10) as response:
        return response.status


async def main():
    urls = [
        'https://www.cnn.com',
        'https://www.baidu.com',
        'https://www.python.org'
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [get_status(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        print(results)


if __name__ == '__main__':
    asyncio.run(main())
