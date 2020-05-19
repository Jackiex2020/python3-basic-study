# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Bb(db.Model):
    __tablename__ = 'bbs'

    autoID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), info='留言标题')
    content = db.Column(db.Text, info='留言内容')
    author = db.Column(db.String(255), info='留言人')
    datetime = db.Column(db.DateTime, server_default=db.FetchedValue(), info='留言时间')
