#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:flask_object_g.py
# author:jackiex
# datetime:2020/9/25 16:57
# software: PyCharm
'''
  flask 框架中的全局变量：g
'''
# import module your need

from flask import Flask, request, g
from common import  funa, funb, func

app = Flask(__name__)


@app.route("/profile")
def my_profile():
    # 从url中取参
    uname = request.args.get('uname')
    # 调用功能函数办理业务
    # 引入g对象
    g.uname = uname
    funa()
    funb()
    func()

    return "办理业务成功"

if __name__ == '__main__':
    app.run(debug=True)