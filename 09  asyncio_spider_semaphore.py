import asyncio
import time

import aiohttp
import blog_spider

# 添加信号量，控制控制并发度
semaphore = asyncio.Semaphore(10)

async def async_craw(url):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                result = await resp.text()
                await asyncio.sleep(5)
                print(f'craw url:{url}', {len(result)})

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    tasks = [
        loop.create_task(async_craw(url))
        for url in blog_spider.urls
    ]

    start = time.time()
    loop.run_until_complete(asyncio.wait(tasks))
    print('time: ', time.time() - start)