#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_mysql-connector1.py
@Time    :   2020/05/01 11:38:03
@Author  :   Jackiex 
@Version :   1.0
'''

# 1 创建数据库使用 "CREATE DATABASE" 语句

import mysql.connector
 
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="123456"
# )
 
# mycursor = mydb.cursor()
 
# mycursor.execute("CREATE DATABASE test_db")

# mycursor.execute("SHOW DATABASES")
 
# for x in mycursor:
#   print(x)

# 2 创建数据表使用 "CREATE TABLE" 语句，创建数据表前，需要确保数据库已存在

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="123456",
#   database="test_db"
# )

# mycursor = mydb.cursor()
 
# #mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")

# mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# 3 插入数据

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="123456",
#   database="test_db"
# )
# mycursor = mydb.cursor()
 
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("中文", "https://www.baidu.com")
# mycursor.execute(sql, val)
 
# mydb.commit()    # 数据表内容有更新，必须使用到该语句
 
# print(mycursor.rowcount, "记录插入成功。")



# 4 批量插入使用 executemany() 方法，
# 该方法的第二个参数是一个元组列表，包含了我们要插入的数据

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="123456",
#   database="test_db"
# )
# mycursor = mydb.cursor()
 
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = [
#   ('Google', 'https://www.google.com'),
#   ('Github', 'https://www.github.com'),
#   ('Taobao', 'https://www.taobao.com'),
#   ('stackoverflow', 'https://www.stackoverflow.com/')
# ]
 
# mycursor.executemany(sql, val)
 
# mydb.commit()    # 数据表内容有更新，必须使用到该语句
 
# print(mycursor.rowcount, "记录插入成功。")


# 5 查询数据使用 SELECT 语句
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="123456",
#   database="test_db"
# )
# mycursor = mydb.cursor()
 
# mycursor.execute("SELECT * FROM sites")
# # mycursor.execute("SELECT name FROM sites")  # 读取指定的字段
 
# myresult = mycursor.fetchall()     # fetchall() 获取所有记录
 
# for x in myresult:
#   print(x)


# 6 如果我们要读取指定条件的数据，可以使用 where 语句
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="123456",
#   database="test_db"
# )

# mycursor = mydb.cursor()
 
# sql = "SELECT * FROM sites WHERE name ='baidu'"
# # sql = "SELECT * FROM sites WHERE url LIKE '%oo%'"

# mycursor.execute(sql)
 
# myresult = mycursor.fetchall()
 
# for x in myresult:
#   print(x)

# 7  查询结果排序可以使用 ORDER BY 语句，
# 默认的排序方式为升序，关键字为 ASC，如果要设置降序排序，可以设置关键字 DESC。

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="123456",
#   database="test_db"
# )
# mycursor = mydb.cursor()
 
# sql = "SELECT * FROM sites ORDER BY name"
# # sql = "SELECT * FROM sites ORDER BY name DESC"

# mycursor.execute(sql)
 
# myresult = mycursor.fetchall()
 
# for x in myresult:
#   print(x)

# 8 如果我们要设置查询的数据量，可以通过 "LIMIT" 语句来指定；

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="123456",
#   database="test_db"
# )

# mycursor = mydb.cursor()
 
# mycursor.execute("SELECT * FROM sites LIMIT 3")

# # 也可以指定起始位置，使用的关键字是 OFFSET：
# # mycursor.execute("SELECT * FROM sites LIMIT 3 OFFSET 1")  # 0 为 第一条，1 为第二条，以此类推

# myresult = mycursor.fetchall()
 
# for x in myresult:
#   print(x) 


# 9 删除记录 使用 "DELETE FROM" 语句

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="test_db"
)
mycursor = mydb.cursor()
 
sql = "DELETE FROM sites WHERE name = 'stackoverflow'"
 
mycursor.execute(sql)
 
mydb.commit()
 
print(mycursor.rowcount, " 条记录删除")

# 10 更新表记录的数据

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="test_db"
)
mycursor = mydb.cursor()
 
sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'"

'''
注意：UPDATE 语句要确保指定了 WHERE 条件语句，否则会导致整表数据被更新。
为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义更新语句的条件：
'''
# sql = "UPDATE sites SET name = %s WHERE name = %s"
# val = ("Zhihu", "ZH") 
# mycursor.execute(sql, val)
  
mycursor.execute(sql)
 
mydb.commit()
 
print(mycursor.rowcount, " 条记录被修改")