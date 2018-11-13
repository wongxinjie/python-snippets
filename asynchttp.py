import time
import asyncio

import aiohttp

NUMBERS = range(12)
URL = 'http://httpbin.org/get?a={}'


async def fetch_async(a):
    async with aiohttp.request('GET', URL.format(a)) as r:
        data = await r.json()

    return data['args']['a']


start = time.time()
event_loop = asyncio.get_event_loop()
tasks = [fetch_async(num) for num in NUMBERS]
results = event_loop.run_until_complete(asyncio.gather(*tasks))

for num, result in zip(NUMBERS, results):
    print('fetch({}) = {}'.format(num, result))

print('Use asyncio+aiohttp cost:', time.time() - start)
