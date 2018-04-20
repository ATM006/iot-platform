#!/usr/bin/python3.5

from flask import Flask
from flask import request,jsonify
from flask_pymongo import PyMongo
import json,uuid,datetime

exp = '{\
"createdDate": "",\
"createdBy": "",\
"token":"",\
"name":"",\
"description":"",\
"metadata": {}\
}'


def site_get_all(mongo):
	sites = mongo.db.sites
	s = sites.find()
	out = []
	for item in s:
		item.pop("_id")
		print(item)
		out.append(item)
	
	return jsonify({'result':out})


def site_get(mongo,token):
	sites = mongo.db.sites
	res = sites.find_one({"token" : token})
	if res == None:
		return '{"site":"not exist!"}'
	else:
		res.pop("_id")
		print(res)
		return jsonify({'result':res})
	#return "site test"

def site_post(mongo,data):
	sites = mongo.db.sites
	date = datetime.datetime.now()
	ex = json.loads(exp)
	token =data["token"]
	if token == '':
		ex["createdDate"] = date.strftime("%Y-%m-%d %H:%M:%S")
		ex["createdBy"] = "admin"
		ex["token"] = str(uuid.uuid1())
		ex["name"] = data["name"]
		ex["description"] = data["description"]
		ex["metadata"] = data["metadata"]
	else:
		return '{"site":"exist"}'
	print(ex)
	sites.insert(ex)
	ex.pop("_id")
	return jsonify({'result':ex})

def site_del(mongo,token):
	sites = mongo.db.sites
	res = sites.find_one({"token" : token})
	if res == None:
		return '{"site":"not exist!"}'
	else:
		sites.remove({"token" : token})
		res.pop("_id")
		print(res)
		return jsonify({'result':res})


