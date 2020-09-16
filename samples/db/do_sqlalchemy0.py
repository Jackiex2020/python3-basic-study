#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_sqlalchemy2.py
@Time    :   2020/05/02 13:12:12
@Author  :   Jackiex 
@Version :   1.0
'''

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  # 父类
from sqlalchemy.orm import sessionmaker


'''
   探究SQLAchemy查询返回的数据类型以及输出问题
'''
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Website(Base):
    __tablename__ = 'website'

    id=sqlalchemy.Column(sqlalchemy.INTEGER,primary_key=True)
    site=sqlalchemy.Column(sqlalchemy.String(50))

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test_db')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建Session:
session = DBSession()

# 创建Query查询，filter是where条件，最后调用first()返回唯一行，如果调用all()则返回所有行:
# user = session.query(User).filter(User.id=='1').first()

# 查看返回的数据类型
# print('type:', type(user))    # 返回的是一个User对象


# print(user.id,user.name)


def main():
    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/mytest')

    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    session=DBSession()
    new_site = Website(id=2, site="www.163.com")
    session.add(new_site) # 添加到session
    session.commit()  # 提交即保存到数据库
    session.close()  # 关闭session
    print('插入数据成功！')

users=session.query(User).all()
# print('type:', type(users))


for user in users:
    print(user.id,user.name)