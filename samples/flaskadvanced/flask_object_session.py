#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:flask_object_session.py
# author:jackiex
# datetime:2020/9/25 16:40
# software: PyCharm

'''
  flask的全局变量使用 session(session是请求上下文的一种,封装了用户信息,可以对数据库中缓存的用户信息进行读写操作)；
  没有设置session时，获取session就是None
'''

from flask import Flask, session

app = Flask(__name__)

"""
    在flask当中使用 session 时，必须要做一个配置、
    即 flask的session中需要用到的秘钥字符串，可以是任意值

    flask默认把数据存放到了cookie中
"""

app.config["SECRET_KEY"] = "ideal"

"""设置session的数据"""
@app.route("/login")
def login():
    session["name"] = "python"
    session["mobile"] = "13512345678"
    return "login success"

@app.route("/index")
def index():
    """获取session的数据"""
    name = session.get("name")
    return "hello %s" % name


if __name__ == '__main__':
    app.run(debug=True)