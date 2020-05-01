#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_mysqldb.py
@Time    :   2020/05/01 12:20:42
@Author  :   Jackiex 
@Version :   1.0
'''

# MySQLdb，是 Python 连接 MySQL 最流行的一个驱动，
# 很多框架都也是基于此库进行开发，遗憾的是它只支持 Python2.x

import MySQLdb

db = MySQLdb.connect(
   host="localhost",  # 主机名
   user="john",     # 用户名
   passwd="megajonhy", # 密码
   db="jonhydb")    # 数据库名称
# 查询前，必须先获取游标
cur = db.cursor()
# 执行的都是原生SQL语句
cur.execute("SELECT * FROM YOUR_TABLE_NAME")
for row in cur.fetchall():
  print(row[0])
db.close()