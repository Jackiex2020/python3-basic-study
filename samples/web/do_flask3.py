#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_flask3.py
@Time    :   2020/05/02 14:56:51
@Author  :   Jackiex 
@Version :   1.0
'''


'''
  前面的例子，是用pymsql模块访问数据的
  那如何SQLAlchemy从数据库中查询数据，传递到前端呢？
'''

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
 

def convert_to_dicts(objs):
    '''把对象列表转换为字典列表'''
    obj_arr = []
     
    for o in objs:
        #把Object对象转换成Dict对象
        dict = {}
        dict.update(o.__dict__)
        obj_arr.append(dict)
     
    return obj_arr



@app.route('/users3')
def userlist3():
    pass
 

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)
    
    