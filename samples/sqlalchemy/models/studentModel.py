#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:studentModel.py
# author:jackiex
# datetime:2020/9/16 11:04
# software: PyCharm
'''
this is function  description
'''
from sqlalchemy import  Column, DateTime, String, or_, Integer
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base
from . import session

from ..utils import commons
from ..utils.response_code import RET

Base = declarative_base()
metadata = Base.metadata

class StudentModel(Base):
    __tablename__ = 'student'

    autoID = Column(Integer, primary_key=True)
    studentID = Column(String(20), info='学生ID')
    name = Column(String(20), info='学生姓名')
    age = Column(Integer, info='学生年龄')
    classID = Column(Integer, info='学生所属班级ID')
    agenda = Column(String(4), info='性别')
    isDelete = Column(Integer,server_default=FetchedValue(), info='是否删除')
    addTime = Column(DateTime, server_default=FetchedValue(), info='记录添加时间')

    @classmethod
    def add_student(cls, **kwargs):
        try:
            student = StudentModel(
                student_ID = kwargs.get('studentID'),
                name = kwargs.get('name'),
                age = kwargs.get('age'),
                classID = kwargs.get('classID'),
                agenda = kwargs.get('agenda')
            )

            session.add(student)
            session.commit()

        except Exception as e:
            session.rollback()
            return {'code': RET.DBERR, 'message': '数据库异常，更新失败', 'error': str(e)}

        return {'code': RET.OK, 'message': 'OK'}

    @classmethod
    def get_student(cls,**kwargs):
        # 获得查询参数
        student_id = kwargs.get('studentID')
        name = kwargs.get('name')
        age = kwargs.get('age')
        agenda = kwargs.get('agenda')
        # page = int(kwargs.get('page', 1))
        # size = int(kwargs.get('size', 10))

        filter_list = []

        # 过滤为空的条件
        if student_id:
            filter_list.append(cls.studentID == student_id)
        if name:
            filter_list.append(cls.name == name)
        if age:
            filter_list.append(cls.age == age)
        if agenda:
            filter_list.append(cls.agenda == agenda)

        try:
            # 多条件分页查询
            # student_model = db.session.query(cls,
            #                                  StudentModel.studentID,
            #                                  StudentModel.name,
            #                                  StudentModel.age,
            #                                  StudentModel.agenda,
            #                                  ClassinfoModel.className
            #                                  ). \
            #     outerjoin(ClassinfoModel, and_(cls.classID == ClassinfoModel.classID)).\
            #     filter(*filter_list).order_by(cls.addTime.desc())
            # count = student_model.count()
            # pages = math.ceil(count / size)
            #
            # students = student_model.limit(size).offset((page - 1) * size).all()

            students = session.query(cls).all()
            # count = students.count()
            # pages = math.ceil(count / size)

            if not students:
                return {'code': RET.NODATA, 'message': '没有学生信息', 'error': '没有学生信息'}

            # 处理返回的数据
            res = commons.query_to_dict(students)

            return {'code': RET.OK, 'message': 'OK', 'data': res}

        except Exception as e:
            return {'code': RET.DBERR, 'message': '数据库异常，获取学生信息失败', 'error': str(e)}