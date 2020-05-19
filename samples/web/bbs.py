#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:bbs.py
# author:jackiex
# datetime:2020/5/15 16:34
# software: PyCharm
'''
   显示留言信息
'''
from flask import Flask,request,render_template,redirect

app = Flask(__name__)

@app.route("/bbs",methods=['GET','POST'])
def index():
    if request.method =='POST':
        username = request.form['username']
        content = request.form['content']
        if username =="tom" and content=="123456":
            return redirect("http://www.baidu.com")
        else:
            message = "Failed Login"
            return render_template('bbs-vue.html',message=message)
    else:
        pass

    return render_template('bbs-vue.html')

if __name__ == '__main__':
    app.run(debug=True)
