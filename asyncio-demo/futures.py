import asyncio


async def slow_func(future):
    await asyncio.sleep(5)
    future.set_result('Future is done!')


async def fast_func():
    print('job done!')


loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_func(future))
loop.run_until_complete(future)
loop.run_until_complete(fast_func())
print(future.result())
loop.close()
