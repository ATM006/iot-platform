#!/usr/bin/python3

from flask import Flask,make_response,redirect,abort
from flask import render_template,request,jsonify
from flask.ext.bootstrap import Bootstrap

import requests,json
import auth
import log


app = Flask(__name__)
bootstrap = Bootstrap(app)

url = 'http://127.0.0.1:5120/iot/spi/'


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
    res = requests.get(url + "sites").json()
    #log.logger.info(res)
    sites = res["result"]
    return render_template('site.html',sites=sites)

@app.route('/tenant')
def tenant():
    res = requests.get(url + "tenants").json()
    #log.logger.info(res)

    return render_template('tenant.html',tenants=res["result"])

@app.route('/device')
def device():
    res = requests.get(url + "devices?type=all").json()
    #log.logger.info(res)

    return render_template('device.html',devices = res["result"])

@app.route('/user/<name>')
def get_user(name):
    res = requests.get(url + "users").json()
    #print(res["result"])
    users = res["result"]

    return render_template('user.html', name=name,users = users)

@app.route('/logout')
def logout():
    return render_template('index.html')







if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8512,debug=False)
