#! /usr/lib/python

from flask import Flask
from flask import request,jsonify
from flask_pymongo import PyMongo 
import json

 
app = Flask(__name__) 
app.config['MONGO1_HOST']='127.0.0.1'
app.config['MONGO1_PORT']=27017
app.config['MONGO1_DBNAME']='iot'
mongo = PyMongo(app,config_prefix='MONGO1') 
 
 
@app.route('/') 
def index(): 
	return 'The IoT '


@app.route('/api/<string:cate>',methods=['GET','POST','PATCH','PUT','DELET'])
def api_cate(cate):
	if request.method == 'GET':
		if cate == 'led':
			li = mongo.db.test_led.find()
			out = []
			for i in li:
				out.append({'led':i['led']})
			return jsonify({'result':out})
			#return "GET\n"

	elif request.method == 'POST':
		
		data = json.loads(request.get_data().decode('utf-8'))
		if cate == 'led':
			leds = mongo.db.test_led
			leds.insert(data)
		
		return "POST\n"

	elif request.method == 'PATCH':
		return "PATCH\n"

	elif request.method == 'PUT':
		return "PUT\n"
		

	elif request.method == 'DELET':
		return "DELET\n"
	





if __name__ == '__main__': 
    app.run(debug=True) 
