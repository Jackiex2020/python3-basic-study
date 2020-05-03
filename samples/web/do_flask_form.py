from flask import Flask,request,render_template,redirect

app = Flask(__name__)


@app.route("/user",methods=['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        if username =="user" and password=="123456":
            return redirect("http://www.baidu.com")
        else:
            message = "Failed Login"
            return render_template('login.html',message=message)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000)