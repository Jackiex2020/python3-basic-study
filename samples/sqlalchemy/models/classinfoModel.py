# coding: utf-8

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class ClassinfoModel(db.Model):
    __tablename__ = 'classinfo'

    autoID = db.Column(db.Integer, primary_key=True)
    classID = db.Column(db.Integer)
    className = db.Column(db.String(255))
