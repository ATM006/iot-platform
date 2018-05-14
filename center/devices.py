#!/usr/bin/python3.5

from flask import Flask
from flask import request,jsonify
from flask_pymongo import PyMongo
import json,uuid,datetime


exp = '{\
"createdDate": "",\
"createdBy": "",\
"hardwareId": "",\
"siteToken":"",\
"comments":"",\
"ext":{},\
"metadata": {}\
}'


def device_get(mongo,devid):
	devices = mongo.db.devices
	ex = json.loads(exp)
	res = devices.find_one({'hardwareId':devid})
	if res == None:
		return jsonify({'result': ex,'code':404})
	else:
		res.pop("_id")
		print(res)
		return jsonify({'result':res,'code':200})

def device_get_by_sitetoken(mongo,typetoken):
	devices = mongo.db.devices
	ex = json.loads(exp)
	res = devices.find({'siteToken':typetoken})
	out = []
	for item in res:
		item.pop("_id")
		print(item)
		out.append(item)

	return jsonify({'result': out, 'code': 200})


def device_get_all(mongo):
	devices = mongo.db.devices
	d = devices.find()
	out = []
	for item in d:
		item.pop("_id")
		print(item)
		out.append(item)

	return jsonify({'result':out,'code':200})


def device_post(mongo,data):
	devices = mongo.db.devices
	date = datetime.datetime.now()
	ex = json.loads(exp)
	devid = data["hardwareId"]
	if devices.find_one({"hardwareId":devid}) == None:
		ex["createdDate"] 	= date.strftime("%Y-%m-%d %H:%M:%S")
		ex["createdBy"] 	= "admin"
		ex["hardwareId"] 	= devid
		ex["siteToken"] 	= data["siteToken"]
		ex["comments"] 		= data["comments"]
		ex["metadata"] 		= data["metadata"]
		ex["ext"] = data["ext"]

		print(ex)
		devices.insert(ex)
		ex.pop("_id")
		return jsonify({'result':ex,'code':200})
	else:
		return jsonify({'result': ex,'code':403})
		

def device_put(mongo,data):
	devices = mongo.db.devices
	date = datetime.datetime.now()
	ex = json.loads(exp)
	devid = data["hardwareId"]
	res = devices.find_one({"hardwareId":devid})
	if res != None:
		devices.remove({"hardwareId": devid})
		res["createdDate"] 	= date.strftime("%Y-%m-%d %H:%M:%S")
		res["createdBy"] 	= "admin"
		res["hardwareId"] 	= devid
		res["siteToken"] 	= data["siteToken"]
		res["comments"] 	= data["comments"]
		res["metadata"] 	= data["metadata"]
		res["ext"] = data["ext"]

		print(res)
		devices.insert(res)
		res.pop("_id")
		return jsonify({'result':res,'code':200})
	else:
		return jsonify({'result': ex,'code':403})



def device_del(mongo,devid):
	devices = mongo.db.devices
	ex = json.loads(exp)
	res = devices.find_one({"hardwareId":devid})
	if res == None:
		return jsonify({'result': ex,'code':404})
	else:
		devices.remove({"hardwareId":devid})
		res.pop("_id")
		print(res)
		return jsonify({'result':res,'code':200})



