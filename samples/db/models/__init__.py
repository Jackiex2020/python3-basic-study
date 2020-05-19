#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2020/05/12 22:50:30
@Author  :   Jackiex 
@Version :   1.0
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config

# 创建引擎
engine = create_engine(config.SQLALCHEMY_DATABASE_URI,
                       pool_size=config.POOL_SIZE,
                       max_overflow=config.MAX_OVERFLOW
                       )

# 创建会话对象
Session = sessionmaker(bind=engine)

# 创建会话实例
session = Session()

