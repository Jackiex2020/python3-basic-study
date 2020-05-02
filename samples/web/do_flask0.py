#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_flask0.py
@Time    :   2020/05/02 10:00:06
@Author  :   Jackiex 
@Version :   1.0
'''

# here put the import lib

from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'this is my web index page!'

@app.route('/myweb')
def myweb():
    return '''
    <html>
    <head>
    <title>Hello</title>
    </head>
    <body>
    <h1>Hello, world!</h1><br><br>
    <a href='/' target="_blank">这个是超链接</a>

    </body>
    </html>
'''

'''
上述例子，这么写html代码，有什么问题？
如何解决？
就是网站的静态资源，如何加载的问题？
'''


# 读取路由中的参数
@app.route('/user/<username>')
def show_user_profile(username):
    return 'hello : %s' % username 


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
    
