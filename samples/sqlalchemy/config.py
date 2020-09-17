#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:config.py
# author:jackiex
# datetime:2020/9/16 11:05
# software: PyCharm
'''
 this is function  description
'''

# 数据库连接配置
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'idealwifi2020'
HOST = '39.107.96.222'
PORT = '3306'
DATABASE = 'BBSDemo'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                                                       PORT, DATABASE)

# 数据库连接定义
#SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:password@ip:3306/test?charset=utf8"

# 数据库连接池初始化的容量
POOL_SIZE = 5

# 连接池最大溢出容量，该容量+初始容量=最大容量。超出会堵塞等待，等待时间为timeout参数值默认30
MAX_OVERFLOW = 10