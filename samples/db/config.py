#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   config.py
@Time    :   2020/05/12 22:45:45
@Author  :   Jackiex 
@Version :   1.0
'''


# 数据库连接定义
SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://xxxx:xxxx@39.107.96.222:3306/BBSDemo?charset=utf8"

# 数据库连接池初始化的容量
POOL_SIZE = 5

# 连接池最大溢出容量，该容量+初始容量=最大容量。超出会堵塞等待，等待时间为timeout参数值默认30
MAX_OVERFLOW = 10