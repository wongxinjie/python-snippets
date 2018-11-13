import threading

import pymysql
import pymysql.cursors
from sql import Table

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='wireless',
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)


def func1():
    account = Table('account')
    print(tuple(account.select(account.password)))


def func2():
    user = Table('user')
    sql = user.select(user.id).where = (user.name == 'wong') & (user.password == '123')
    print(tuple())


t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()
