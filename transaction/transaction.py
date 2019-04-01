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
    conn.begin()
    with conn.cursor() as cursor:
        sql = "INSERT INTO `user`(`name`, `email`, `mobile`, `salt_password`) VALUES (%s, %s, %s, %s);"
        cursor.execute(sql, ('xinjie', 'hgxinjie@163.com',  mobile, '1111111111111'))
    time.sleep(10)
    conn.commit()
    e = time.time()
    print('start: {}, end: {}, esplice: {}'.format(s, e, e - s))
