#! /usr/lib/python

from flask import Flask
from flask import request,jsonify
#from flask_pymongo import PyMongo 
import json,log,rediser
import requests

import data,commands


urlt = 'http://127.0.0.1:5120/iot/spi/devices/'
 
app = Flask(__name__) 
 
 
@app.route('/') 
def index(): 
	return 'The IoT API'

'''
@app.route('/iot/api/devices/<string:hardwareId>/events/<string:etype>',methods=['POST'])
def api_events_post(hardwareId,etpye):
	log.logger.info("call : api_events_post()")
	dat = json.loads(request.get_data().decode('utf-8'))

	if etpye != dat["eventType"]:
		return jsonify({'result': None, 'code': 403})

	if dat["eventType"] == "DevicesData":
		res = data.data_post_process(hardwareId,dat)

	elif dat["eventType"] == "UserCommands":
		res = commands.commands_post_process(hardwareId,dat)

	else:
		res = jsonify({'result': None, 'code': 403})

	return res
'''


@app.route('/iot/api/devices/<string:hardwareId>/events/<string:etype>', methods=['GET','POST'])
def api_events_get(hardwareId,etype):
	if request.method == 'GET':
		if etype == "DevicesData":
			res = data.data_get_process(hardwareId)

		elif etype == "UserCommands":
			res = commands.commands_get_process(hardwareId)

		else:
			res = jsonify({'result': None, 'code': 403})

		return res

	elif request.method == 'POST':
		dat = json.loads(request.get_data().decode('utf-8'))

		if etype != dat["eventType"]:
			return jsonify({'result': None, 'code': 403})

		if dat["eventType"] == "DevicesData":
			res = data.data_post_process(hardwareId, dat)

		elif dat["eventType"] == "UserCommands":
			res = commands.commands_post_process(hardwareId, dat)

		else:
			res = jsonify({'result': None, 'code': 403})

		return res



if __name__ == '__main__': 
	#app.run(host='0.0.0.0',port=5211,debug=False)
	from werkzeug.contrib.fixers import ProxyFix
	app.wsgi_app = ProxyFix(app.wsgi_app)
	app.run()
