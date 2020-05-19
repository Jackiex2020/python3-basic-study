#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   bbsModel.py
@Time    :   2020/05/12 22:44:10
@Author  :   Jackiex 
@Version :   1.0
'''
from sqlalchemy import BigInteger, Column, DateTime, String, or_
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base
from . import session

from ..utils import commons
from ..utils.response_code import RET

Base = declarative_base()
metadata = Base.metadata



class BBsModel(Base):
    __tablename__ = 'bbs'

    autoID = Column(BigInteger, primary_key=True)    
    username = Column(String(255, 'utf8_general_ci'), info='留言者')  
    content = Column(String(1000, 'utf8_general_ci'), info='留言内容')
    addTime = Column(DateTime, server_default=FetchedValue(), info='记录添加时间')

    @classmethod
    def add_bbs(cls, **kwargs):       
        try:
            bbs_model = BBsModel(
                    username=kwargs.get('username'),
                    content=kwargs.get('content')
                )
      
            session.add(bbs_model)
            session.commit()

        except Exception as e:
            session.rollback()
            return {'code': RET.DBERR, 'message': '数据库异常，更新失败', 'error': str(e)}

        return {'code': RET.OK, 'message': 'OK'}

    @classmethod
    def get_bbs(cls, **kwargs):

        page = int(kwargs.get('page', 1))
        size = int(kwargs.get('size', 10))
        try:
            filter_list = []
            filter_list.append(or_(cls.username == '', cls.content == None))

            bbs_model = session.query(cls).filter(*filter_list)

            bbs_contents = bbs_model.limit(size).offset((page - 1) * size).all()

            if not bbs_contents:
                return {'code': RET.NODATA, 'message': '无企业数据', 'error': '无企业数据'}
        except Exception as e:
            return {'code': RET.DBERR, 'message': '数据库异常，查询失败', 'error': str(e)}

        return {'code': RET.OK, 'message': 'OK', 'data': commons.all_to_dict(bbs_contents)}