#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_mysql-0.py
@Time    :   2020/05/01 08:40:24
@Author  :   Jackiex 
@Version :   1.0
'''
'''
  mysql-connector 是 MySQL 官方提供的驱动器
'''
# 1 可以使用以下代码来连接数据库：

import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="123456"   # 数据库密码
)
 
print(mydb)






# 数据库操作代码一般结构
conn = mysql.connector.connect(
    host="localhost",       # 数据库主机地址
    user='root', 
    password='123456',
    database='test'
)

cursor = conn.cursor()

# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
print('rowcount =', cursor.rowcount)

# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)

# 关闭Cursor和Connection:
cursor.close()
conn.close()



