#!/usr/bin/python3

from flask import Flask,make_response,redirect,abort
from flask import render_template,request,jsonify
from flask.ext.bootstrap import Bootstrap

import auth
import log


app = Flask(__name__)
bootstrap = Bootstrap(app)


'''index() 函数注册为程序根地址的处理程序'''
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    log.logger.info("call : login()")
    if request.method == 'POST':
        log.logger.debug("login post method")
        username = request.form['username']
        password = request.form['password']

        if auth.authority_user(username,password):
            return render_template('console.html')

        else:
            #return jsonify({'status': '-1', 'errmsg': '用户名或密码错误！'})
            pass

    return render_template('login.html')


@app.route('/console')
def console():
    return render_template('console.html')


@app.route('/logout')
def logout():
    return render_template('index.html')

@app.route('/user/<name>')
def get_user(name):
    return render_template('user.html', name=name)





if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8512,debug=False)
