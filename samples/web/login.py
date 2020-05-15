#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:login.py
# author:jackiex
# datetime:2020/5/15 16:24
# software: PyCharm
'''
this is function  description 
'''
from flask import Flask,request,render_template,redirect

app = Flask(__name__)

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        if username =="tom" and password=="123456":
            return redirect("http://www.baidu.com")
        else:
            message = "Failed Login"
            return render_template('login.html',message=message)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)