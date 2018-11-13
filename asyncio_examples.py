import asyncio


def noop(loop):
    print('noop')
    loop.stop()


loop = asyncio.get_event_loop()
loop.call_soon(noop, loop)
print('begin run server')
loop.run_forever()
loop.close()
