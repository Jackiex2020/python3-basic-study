#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:flask_api.py
# author:jackiex
# datetime:2020/5/19 18:34
# software: PyCharm
'''
this is function  description 
'''
import json

from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import *

app = Flask(__name__)

CORS(app, supports_credentials=True)


app.config.from_object('myconfig')
db = SQLAlchemy(app)

class BbsModel(db.Model):
    __tablename__ = 'bbs'

    autoID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), info='留言标题')
    content = db.Column(db.Text, info='留言内容')
    author = db.Column(db.String(255), info='留言人')
    createtime = db.Column(db.DateTime, server_default=db.FetchedValue(), info='留言时间')


    # 单个对象方法1
    def to_dict(self):
        model_dict = dict(self.__dict__)
        del model_dict['_sa_instance_state']
        return model_dict

    # 单个对象方法2
    def single_to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # 多个对象
    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result

# 配合多个对象使用的函数
def to_json(all_vendors):
    v = [ven.dobule_to_dict() for ven in all_vendors]
    return v

@app.route('/get')
def getUser():
    bbs = BbsModel.query.all()
    data = to_json(bbs)
    return Response(json.dumps(data), mimetype='application/json')


if __name__ == '__main__':
    app.run()
