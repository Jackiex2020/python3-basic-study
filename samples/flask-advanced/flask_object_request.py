#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:flask_object_request.py
# author:jackiex
# datetime:2020/9/25 15:25
# software: PyCharm
'''
  学习request对象
'''

from flask import Flask, redirect, render_template, jsonify
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    print('请求头:%s' % request.headers)  # 打印结果为请求头信息
    print('请求方式:%s' % request.method)  # GET
    print('请求url地址:%s' % request.url)  # 请求url地址:http://127.0.0.1:5000/

    # 打印:ImmutableMultiDict([('file1', <FileStorage: '1.txt' ('text/plain')>)])

    # 保存文件
    # get('file1')中的'file1'名称要与postman中的key值保持一致
    # 否则会出现报错:'NoneType' object has no attribute 'save'
    # file = request.files.get('file1')
    # file.save('./static/aaa.txt')

    print('cookie值:%s' % request.cookies)  # 暂时还没设置cookie值,打印结果为:{}

    return 'hello world'


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    print('请求方式为------->', request.method)
    args = request.args.get("name") or "args没有参数"
    print('args参数是------->', args)
    form = request.form.get('name') or 'form 没有参数'
    print('form参数是------->', form)
    return jsonify(args=args, form=form)

'''
    注意这里：如果想要得到data里面的name的值，直接使用request.data.get('name')
    是得不到值的，
    需要使用request.json.get('name')
    才能获取到数据，项目中觉得request.json经常会用到。

    补充：json.dumps(data) = > 字典转字符串
    json.loads(data) = > 字符串转字典
'''


@app.route("/login",methods=['GET','POST'])
def login():

    if request.method =='POST':
        print('请求url地址:%s' % request.url)
        print('请求数据:%s' % request.data)  # 请求数据:b'{name:"zs",age:18}'
        print('账号:%s' % request.form.get('username'))  # 表单:"login"
        print('密码:%s' % request.form.get('password'))  # 参数:12345
        #print('文件:%s' % request.files)

        username = request.form['username']
        password = request.form['password']
        if username =="user" and password=="123456":
            return redirect("http://www.baidu.com")
        else:
            message = "Failed Login"
            return render_template('login.html',message=message)
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
