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
            #return render_template('tenant.html')
            return redirect("/tenant")

        else:
            return jsonify('404.html')

    return render_template('login.html')


@app.route('/console')
def console():
    return render_template('console.html')

@app.route('/site')
def site():
    return render_template('site.html')

@app.route('/tenant')
def tenant():
    tenants =[
        {
            "authenticationToken": "",
            "authorizedUserIds": [
                "admin"
            ],
            "createdBy": "admin",
            "createdDate": "2018-04-20 20:25:53",
            "id": "test1",
            "metadata": {},
            "name": "test tenant"
        },
        {
            "authenticationToken": "",
            "authorizedUserIds": [
                "admin"
            ],
            "createdBy": "admin",
            "createdDate": "2018-04-26 11:46:23",
            "id": "test id",
            "metadata": {},
            "name": "test tenant xatu"
        },
        {
            "authenticationToken": "123",
            "authorizedUserIds": [
                "admin"
            ],
            "createdBy": "admin",
            "createdDate": "2018-05-04 09:54:48",
            "id": "test",
            "metadata": {},
            "name": "test tenant"
        }
    ]

    return render_template('tenant.html',tenants=tenants)

@app.route('/device')
def device():
    return render_template('device.html')

@app.route('/user/<name>')
def get_user(name):
    name = [
        {
            'name': u'红楼梦',
            'author': u'曹雪芹',
            'price': 200
        },
        {
            'name': u'水浒传',
            'author': u'施耐庵',
            'price': 100
        },
        {
            'name': u'三国演义',
            'author': u'罗贯中',
            'price': 120
        },
        {
            'name': u'西游记',
            'author': u'吴承恩',
            'price': 230
        }
    ]
    return render_template('user.html', name=name)

@app.route('/logout')
def logout():
    return render_template('index.html')







if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8512,debug=False)
