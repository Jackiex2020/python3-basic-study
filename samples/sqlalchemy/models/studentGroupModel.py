# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class StudentGroup(db.Model):
    __tablename__ = 'student_group'

    autoID = db.Column(db.Integer, primary_key=True)
    groupID = db.Column(db.Integer, info='社团编号')
    studentID = db.Column(db.String(20), info='学生学号')
    groupName = db.Column(db.String(50), info='社团名称')
    joinlTime = db.Column(db.DateTime, info='加入社团时间')
