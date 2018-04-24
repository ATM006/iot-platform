#! /usr/lib/python

from flask import Flask
from flask import request,jsonify
#from flask_pymongo import PyMongo 
import json,log,rediser
import requests

#import events


urlt = 'http://127.0.0.1:5120/iot/spi/devices/'
 
app = Flask(__name__) 
 
 
@app.route('/') 
def index(): 
	return 'The IoT API'


@app.route('/iot/api/devices/<string:hardwareId>/events/',methods=['POST','GET'])
def api_events(hardwareId):
	#log.logger.info("call api_events()")
	rpool = rediser.redis_pool
	if request.method == 'POST':
		data = json.loads(request.get_data().decode('utf-8'))
		rpool.set(hardwareId,data)
		res = requests.post(urlt + hardwareId + "/events/",request.get_data())
		res = res.json()
		return jsonify({'result':res})
		
	elif request.method == 'GET':
		res = rpool.get(hardwareId)
		if res != None:
			return res
		else:
			res = requests.get(urlt + hardwareId + "/events/")
			res = res.json()
			return jsonify({'result':res})


if __name__ == '__main__': 
    app.run(host='0.0.0.0',port=8080,debug=False) 
