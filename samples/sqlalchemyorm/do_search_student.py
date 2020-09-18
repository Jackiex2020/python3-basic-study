# -*- coding:utf-8 -*-

# file: do_search_student.py
# author: zhangzhuanghua
# datetime: 2020/9/17 9:36
# software: PyCharm

from sqlalchemy import and_, or_
from samples.sqlalchemyorm.models.classinfoModel import ClassinfoModel
from samples.sqlalchemyorm.models.studentModel import StudentModel
from samples.sqlalchemyorm.models import session
from samples.sqlalchemyorm.utils import commons

# 1 单表查询---获取单表全部学生记录的查询，分页显示；
def query1():
    res1 = StudentModel().get_all_student()
    if res1.get('code') == '200':
        print(res1.get('data'))

# 2 两个表联合查询--获取学生完整信息（学生信息和班级名称）的查询；分页显示；
def query2():
    res2 = StudentModel.double_table()
    if res2.get('code') == '200':
         print(res2.get('data'))


# 3 三个表关联查询--获取学生完整信息（学生信息和班级名称），并显示学生参加了哪些社团（一个学生会参加多个社团）；
def query3():
    res3 = StudentModel.triple_table_search()
    print(res3)


# 其他简单查询
def query_simple():
    student_models = session.query(StudentModel).all()
    print(student_models)  # 返回对象列表
    print(commons.all_to_dict(student_models))  # 返回字典列表

    student_models = session.query(StudentModel.name, StudentModel.age).all()
    print(student_models)  # 返回元组列表

# 带条件查询
def query_condition():
    print(commons.all_to_dict(session.query(StudentModel).filter_by(name='张三').all()))
    print(commons.all_to_dict(session.query(StudentModel).filter(StudentModel.name == "张三").all()))
    print(commons.all_to_dict(session.query(StudentModel).filter(StudentModel.name.like("张%")).all()))


# 多条件查询
def query_conditions():
    # 类似SQL中的and条件
    print(commons.all_to_dict(session.query(StudentModel).filter(and_(StudentModel.name.like("张%"),
                                                                      StudentModel.isDelete == 0)).all()))
    # 类似SQL中的 or条件
    print(commons.all_to_dict(session.query(StudentModel).filter(or_(StudentModel.name.like("张%"),
                                                                     StudentModel.classID == 2)).all()))

if __name__ == '__main__':
   # query1()
   # query2()
   # query3()
   query_simple()