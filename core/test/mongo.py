#! /usr/lib/python

from flask import Flask
from flask_pymongo import PyMongo 

 
app = Flask(__name__) 
app.config['MONGO1_HOST']='127.0.0.1'
app.config['MONGO1_PORT']=27017
app.config['MONGO1_DBNAME']='iot'
mongo = PyMongo(app,config_prefix='MONGO1') 
 
 
@app.route('/') 
def index(): 
	return 'Index Page'


#插入数据[这里指定了数据]
@app.route('/add/')          #后面加入了一个"/"作用跟不加的效果自己可以测试。
def add(): 
    leds = mongo.db.test_led
    leds.insert({"led":"false"}) 
 


#查询数据，通过后面的<username>传入要查询的用户名 
@app.route('/find/<led>') 
def find(led): 
    leds = mongo.db.test_led 
    led_state = leds.find_one({"led":led}) 
    if led_state: 
        return "你查找的用户名：" + led["led"]
    else: 
        return "你查找的用户并不存在!" 
"""
 
#更新数据[monogodb版本可能有所不同] 
@app.route('/update/<username>') 
def update(username): 
    user = mongo.db.users 
    passwd = "abcd10023" 
    userusername = user.find_one({"username":username}) 
    username["password"] = passwd 
    user.save(username) 
    return "Update OK " + username["username"] 
 
#删除数据 
@app.route('/delete/<username>') 
def delete(username): 
    user = mongo.db.users 
    userusername = user.find_one({"username":username}) 
    user.remove(username) 
    if username: 
        return "Remove " + username["username"] + " Ok!" 
    else: 
        return "用户不存在，请核对后再操作!" 
"""

 
if __name__ == '__main__': 
    app.run(debug=False) 
