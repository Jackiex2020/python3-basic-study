#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_pymsql.py
@Time    :   2020/05/01 12:22:20
@Author  :   Jackiex 
@Version :   1.0
'''

# here put the import lib

import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","123456","test_db" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()

