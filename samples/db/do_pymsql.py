#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_pymsql.py
@Time    :   2020/05/01 12:22:20
@Author  :   Jackiex 
@Version :   1.0
'''

# here put the import lib

# import pymysql
 
# # 打开数据库连接
# db = pymysql.connect("localhost","root","123456","test_db" )
 
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
 
# # 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT VERSION()")
 
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
 
# print ("Database version : %s " % data)
 
# # 关闭数据库连接
# db.close()

'''
  -----------规范写法，增加数据库操作的异常处理；注意，所有的操作都可能会失败---------
'''
import pymysql
import traceback
 
# 打开数据库连接
db = pymysql.connect("localhost","root","123456","mytest" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 插入语句
sql = """INSERT INTO user(name,age)
         VALUES ('cynthia',21)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except Exception as e:
   # 异常信息的处理：1直接抛出；2 打印提示输出
   # raise e 
   #print("发生异常",e)  
   #输出异常信息  
   # traceback.print_exc() 
   #3 将错误日志输入到目录文件中  
    # f = open("log.txt", "a")
    # traceback.print_exc(file=f)
    # f.flush()
    # f.close()
    # # 如果发生错误则回滚
    # db.rollback()
  
finally: 
# 关闭数据库连接
   db.close()