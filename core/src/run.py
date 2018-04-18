#! /usr/lib/python

from flask import Flask
from flask import request,jsonify
from flask_pymongo import PyMongo 
import json

import leds
import sites
import users
import events
import devices


 
app = Flask(__name__) 
app.config['MONGO1_HOST']='127.0.0.1'
app.config['MONGO1_PORT']=27017
app.config['MONGO1_DBNAME']='iot'
mongo = PyMongo(app,config_prefix='MONGO1') 
 
 
@app.route('/') 
def index(): 
	return 'The IoT '


@app.route('/iot/api/<string:cate>',methods=['GET','POST','PATCH','PUT','DELET'])
def api_cate(cate):
	if request.method == 'GET':
		if cate == 'led':
			res = leds.led_get(mongo)

		elif cate == 'sites':
			res = sites.site_get(mongo)

		elif cate == 'users':
			res = users.user_get(mongo)

		elif cate == 'devices':
			res = devices.device_get(mongo)

		return res
		
	elif request.method == 'POST':
		data = json.loads(request.get_data().decode('utf-8'))
		if cate == 'led':
			res = leds.led_post(mongo,data)

		elif cate == 'sites':
			res = sites.site_post(mongo,data)
	
		elif cate == 'users':
			res = users.user_post(mongo,data)
		
		elif cate == 'devices':
			res = devices.device_post(mongo,data)

		return res

	elif request.method == 'PATCH':

		return "PATCH\n"

	elif request.method == 'PUT':

		return "PUT\n"
		
	elif request.method == 'DELET':
		if cate == 'sites':
			res = sites.site_del(mongo)

		elif cate == 'users':
			res = users.user_del(mongo)

		elif cate == 'devices':
			res = devices.device_del(mongo)

		return res
	


@app.route('/iot/api/devices/<int:hardwareId>/events/',methods=['POST','GET'])
def api_events(hardwareId):
	if request.method == 'POST':
		data = json.loads(request.get_data().decode('utf-8'))
		res = events.event_post(mongo,data,hardwareId)
		return res
	elif request.method == 'GET':
		res = events.event_get(mongo,hardwareId)
		return res




if __name__ == '__main__': 
    app.run(debug=False) 
