#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



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

'''
1  连接数据库，并对已有的表插入记录
'''

# session = DBSession()  # 创建session对象
# # 创建新User对象:
# new_user = User(id='5', name='Bob')

# session.add(new_user) # 添加到session

# session.commit()  # 提交即保存到数据库


# session.close()  # 关闭session


'''
2   连接数据库，查询记录并输出
'''

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()
