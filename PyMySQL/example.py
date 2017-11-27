#!/usr/bin/env python
from __future__ import print_function

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='***', passwd='***', db='pondplug')

cur = conn.cursor()

cur.execute("SELECT * FROM pondplug.pond_solution")

print(cur.description)

print()

for row in cur:
    print(row)

cur.close()
conn.close()
