#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_sqlalchemy0.py
@Time    :   2020/05/01 18:18:39
@Author  :   Jackiex 
@Version :   1.0
'''

# here put the import lib

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base   # 父类

Base=declarative_base()

class User(Base):
    __tablename__ = 'user'

    id=sqlalchemy.Column(sqlalchemy.INTEGER)
    site=sqlalchemy.Column(sqlalchemy.String(50))


def main():
    pass

if __name__ == '__main__':
    main()
                
        