import threading

from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/bidongv2?charset=utf8',
                       pool_size=10)


def query(worker):
    print('worker - {} run query'.format(worker))
    conn = engine.connect()
    rv = conn.execute('SELECT COUNT(*) FROM `bd_account`;')
    print(rv.fetchall())


threads = [threading.Thread(target=query, args=(n,)) for n in range(20)]
for t in threads:
    t.start()

for t in threads:
    t.join()
