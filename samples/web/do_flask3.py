#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask,Response,jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
import json

from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config.from_object('myconfig')
db = SQLAlchemy(app)

class User(db.Model):
    # 表的名字:
    __tablename__ = 'user3'

    # 表的结构:
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
 
def model_to_dict(result):
    from collections.abc import Iterable, Iterator
    # 转换完成后，删除 '_sa_instance_state' 特殊属性
    try:
        if isinstance(result, Iterable):
            tmp = [dict(zip(res.__dict__.keys(), res.__dict__.values())) for res in result]
            for t in tmp:
                t.pop('_sa_instance_state')
        else:
            tmp = dict(zip(result.__dict__.keys(), result.__dict__.values()))
            tmp.pop('_sa_instance_state')
        return tmp
    except BaseException as e:
        print(e.args)
        raise TypeError('Type error of parameter')

@app.route('/')
def home():
    users=db.session.query(User).all()
    users_dict=model_to_dict(users)
    
    # users_json=jsonify(users_dict)
    
    # print(users_json)    
    # return users_json
    return render_template('users3.html',mydict=users_dict)


if __name__ == '__main__':
    app.run(debug=True, port=5000)