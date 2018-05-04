#! /usr/lib/python

from flask import Flask
from flask import request,jsonify
#from flask_pymongo import PyMongo
import json,log
import requests


urlt = 'http://127.0.0.1:5120/iot/spi/'
urls = 'http://127.0.0.1:5120/iot/spi/devices'

app = Flask(__name__) 
 
 
@app.route('/')
def index(): 
	return 'The IoT ADMIN'

#租户、站点、设备、用户管理接口
@app.route('/iot/api/<string:cate>',methods=['GET','POST','PATCH','PUT','DELET'])
def api_cate(cate):
	log.logger.info("call : api_cate(cate)")
	if request.method == 'GET':
		res = requests.get(urlt + cate)
		res = res.json()
		log.logger.info(res)
		return jsonify(res)


	elif request.method == 'POST':
		data = json.loads(request.get_data().decode('utf-8'))
		res = requests.post(urlt + cate,request.get_data())
		res = res.json()
		log.logger.info(res)
		return jsonify(res)

	elif request.method == 'PATCH':

		return "PATCH\n"

	elif request.method == 'PUT':
		data = json.loads(request.get_data().decode('utf-8'))
		res = requests.put(urlt + cate,request.get_data())
		res = res.json()
		log.logger.info(res)
		return jsonify(res)
		
	elif request.method == 'DELET':

		return "DELETE\n"
	

@app.route('/iot/api/<string:cate>/<string:cateid>',methods=['GET','DELET'])
def api_cate_id(cate,cateid):
	if request.method == 'GET':
		res = requests.get(urlt + cate + "/" + cateid)
		res = res.json()
		log.logger.info(res)
		return jsonify(res)

	elif request.method == 'DELET':
		res = requests.delete(urlt + cate + "/" + cateid)
		print(res.text)
		#res = res.json()
		#log.logger.info(res)
		#return jsonify(res)
		return  "TEST\n"



if __name__ == '__main__': 
    app.run(host='0.0.0.0',port=8080,debug=False)
