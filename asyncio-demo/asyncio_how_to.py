import asyncio


async def create():
    await asyncio.sleep(3.0)
    print("(1) create file")


async def write():
    await asyncio.sleep(1.0)
    print("(2) write file")


async def close():
    print("(3) close file")


async def main():
    await asyncio.ensure_future(create())
    await asyncio.ensure_future(write())
    await asyncio.ensure_future(close())
    await asyncio.sleep(2.0)
    loop.stop()


loop = asyncio.get_event_loop()
asyncio.ensure_future(main())
loop.run_forever()
print("Pending tasks at exit: %s" % asyncio.Task.all_tasks(loop))
loop.close()
