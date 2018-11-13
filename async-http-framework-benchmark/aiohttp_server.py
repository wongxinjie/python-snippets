import uuid

import aiomysql
from aiohttp import web


app = web.Application()

async def init_mariadb(app):
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='', db='benchmark')
    app['db'] = pool


async def close_mariadb(ap):
    app['db'].close()
    await app['db'].wait_closed()


app.on_startup.append(init_mariadb)
app.on_cleanup.append(close_mariadb)


async def gen_tokens(db, request_id, count):
    with await db as conn:
        cursor = await conn.cursor()
        rvs = [(request_id, str(uuid.uuid4())[:8]) for _ in range(count)]
        sql = "INSERT INTO token (request_id, token) VALUES(%s, %s)"
        await cursor.executemany(sql, rvs)
        return await cursor.execute("COMMIT;")


async def token_count(db):
    with await db as conn:
        cursor = await conn.cursor()
        sql = "SELECT request_id, COUNT(id) FROM token GROUP BY request_id"
        await cursor.execute(sql)
        rvs = await cursor.fetchall()

    data = {rv[0]: rv[1] for rv in rvs}
    if data:
        data['total'] = sum(data.values())
    else:
        data['total'] = 0
    return data


class TokenView(web.View):

    async def get(self):
        pool = self.request.app['db']
        payload = await token_count(pool)
        return web.json_response(payload)

    async def post(self):
        pool = self.request.app['db']
        count = self.request.query.get('count')
        request_id = str(uuid.uuid4())
        rv = await gen_tokens(pool, request_id, int(count))
        print(rv)
        return web.json_response({"status_code": 200})

app.router.add_route('*', '/v1.0/tokens', TokenView)
web.run_app(app, host='localhost', port=8080)
