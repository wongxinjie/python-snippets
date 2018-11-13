import asyncio


async def factor(name, number):
    f = 1
    for i in range(2, number+1):
        print("Task %s: Compute factor(%s)..." % (name, i))
        await asyncio.sleep(1)
        f *= i
    print('Task %s: factor(%s) = %s' % (name, number, f))


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    factor('A', 2),
    factor('B', 3),
    factor('C', 4),
))
loop.close()
