#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_sqlalchemy0.py
@Time    :   2020/05/01 18:18:39
@Author  :   Jackiex 
@Version :   1.0
'''
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  # 父类
from sqlalchemy.orm import sessionmaker

Base=declarative_base()

class Website(Base):
    __tablename__ = 'website'

    id=sqlalchemy.Column(sqlalchemy.INTEGER,primary_key=True)
    site=sqlalchemy.Column(sqlalchemy.String(50))


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

if __name__ == '__main__':
    main()
                
        