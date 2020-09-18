#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:do_student.py
# author:jackiex
# datetime:2020/9/16 18:50
# software: PyCharm
'''
this is function  description 
'''
# import module your need

from samples.sqlalchemy.models.studentModel import StudentModel

if __name__ == '__main__':

    # 测试添加数据
    kwargs = {
        'studentID': '23462327',
        'name': '哈哈哈',
        'age':20,
        'classID': 1,
        'agenda':'女'
    }

    result_dict = StudentModel.add_student(**kwargs)

    if result_dict.get('code') == '200':
        print("插入记录成功")

