#!/usr/bin/env python
"""
    transaction.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    :author: wongxinjie
    :copyright: (c) 2019, Tungee
    :date created: 2019-04-01 14:14
    :python version: Python3.6
"""
import time
import random

import pymysql
import pymysql.cursors

conn = pymysql.connect(
    host='localhost',
    user='root',
    port=3306,
    password='',
    db='rebegin',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


def execute_with_transaction(mobile):
    s = time.time()
    conn.autocommit(False)
    conn.begin()
    with conn.cursor() as cursor:
        sql = "INSERT INTO `user`(`name`, `email`, `mobile`, `salt_password`, `count`) VALUES (%s, %s, %s, %s, %s);"
        print('xinjie', 'hgxinjie@163.com',  mobile, '1111111111111', 10)
        cursor.execute(sql, ('xinjie', 'hgxinjie@163.com',  mobile, '1111111111111', 10))
    conn.commit()
    e = time.time()
    print('start: {}, end: {}, esplice: {}'.format(s, e, e - s))


def update_with_transaction(mobile):
    count = random.randint(1, 100)
    conn.autocommit(False)
    conn.begin()
    print('begin ', time.time())
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE `user` SET `count` = `count` + %s WHERE `mobile` = %s"
            cursor.execute(sql, (count, mobile))
        time.sleep(10)
        conn.commit()
    except Exception as err:
        print(err)
        conn.rollback()
    print('end ', time.time())



# execute_with_transaction('18825111143')
# execute_with_transaction('18825111142')


