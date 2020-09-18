#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:__init__.py.py
# author:jackiex
# datetime:2020/9/16 11:04
# software: PyCharm
'''
this is function  description 
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .. import config  #从上一层文件夹导入文件


# 创建引擎
engine = create_engine(config.SQLALCHEMY_DATABASE_URI,
                       pool_size=config.POOL_SIZE,
                       max_overflow=config.MAX_OVERFLOW
                       )

# 创建会话对象
Session = sessionmaker(bind=engine)

# 创建会话实例
session = Session()