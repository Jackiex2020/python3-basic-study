#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_flask1.py
@Time    :   2020/05/02 10:53:19
@Author  :   Jackiex 
@Version :   1.0
'''

'''
上述例子，这么写html代码，有什么问题？如何解决？
就是网站的静态资源，如何加载的问题？
flask框架当然有解决方案：
只要在你的包中或是模块的所在目录中创建一个名为 static 的文件夹，
在应用中使用 /static 即可访问
'''

from flask import Flask,render_template
import time

app=Flask(__name__)

@app.route('/')
def index():
    return 'this is my web index page!'

@app.route('/hello')
def hello():
    return render_template('hello.htm')

'''
上述例子实现了后台代码和前端代码的分离
那如何将数据，传到前端页面上去？
'''

@app.route('/hellodata')
def hellodata():
    user_name='Jackiex'
    return render_template('hellodata.htm',name=user_name)

'''
那如何传递多个数据到前端呢？
'''

@app.route('/data')
def data():
    class Person(object):
        Email = 'XXX@XXX.com';
        time = time.time();

    dell=Person()

    context={
        'username':"jackiex",
        'age': "18",
        'gender': "男",
        'flag': "王者",
        'hero': "猴子",
        'person':dell,
        'wwwurl':{
            'baidu':'www.baidu.com',
            'google':'www.google.com'
        }
    }
    
    return render_template('datas.htm',**context)

'''
  上面的例子，是写死的数据，传递到前端显示
  那如何从数据库中查询数据，传递到前端呢？
'''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    