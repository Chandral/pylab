#!/usr/bin/env python
# input("Example Input: ")

import datetime as dt

a = {"A": 1, "B": "TEST", "C":dt.datetime.now()}

sql_part1 = "INSERT INTO table ("
sql_part2 = "VALUES ("
for k, v in a.items():
    sql_part1 += k + ','
    if isinstance(v, str):
        sql_part2 += v + ','
    else:
        sql_part2 += str(v) + ','



sql_part1 += ')'
sql_part2 += ')'
print(sql_part1[:-1])
