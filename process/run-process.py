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


@app.route('/iot/api/devices/<string:hardwareId>/events/',methods=['POST'])
def api_events_post(hardwareId):
	log.logger.info("call : api_events_post()")

	dat = json.loads(request.get_data().decode('utf-8'))
	if dat["eventType"] == "DevicesData":
		res = data.data_post_process(hardwareId,dat)
		return res
	elif dat["eventType"] == "UserCommands":
		res = commands.commands_post_process(hardwareId,dat)
		return res

@app.route('/iot/api/devices/<string:hardwareId>/events/<string:type>/', methods=['GET'])
def api_events_get(hardwareId,type):
	log.logger.info("call : api_events_get()")

	if type == "DevicesData":
		res = data.data_get_process(hardwareId)
		return res

	elif type == "UserCommands":
		res = commands.commands_get_process(hardwareId)
		return res


if __name__ == '__main__': 
	app.run(host='0.0.0.0',port=5211,debug=False)
