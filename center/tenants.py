#!/usr/bin/python3.5

from flask import Flask
from flask import request,jsonify
from flask_pymongo import PyMongo
import json,uuid,datetime

import log


exp = '{\
"createdDate":"",\
"createdBy":"",\
"id":"",\
"name":"",\
"authenticationToken":"",\
"authorizedUserIds":[],\
"ext":{},\
"metadata":{}\
}'



def tenant_get(mongo,tenantId):
	tenants = mongo.db.tenants
	ex = json.loads(exp)
	res = tenants.find_one({"id":tenantId})
	if res == None:
		return jsonify({'result': ex,'code':404})
	else:
		res.pop("_id")
		print(res)
		return jsonify({'result':res,'code':200})


def tenant_get_all(mongo):
	tenants = mongo.db.tenants
	t = tenants.find()
	out = []
	for item in t:
		item.pop("_id")
		print(item)
		out.append(item)

	return jsonify({'result':out,'code':200})


def tenant_post(mongo,data):
	tenants = mongo.db.tenants
	date = datetime.datetime.now()
	ex = json.loads(exp)
	tenantId = data["id"]
	if tenants.find_one({"id":tenantId}) == None:
		ex["createdDate"] = date.strftime("%Y-%m-%d %H:%M:%S")
		ex["createdBy"] = "admin"
		ex["id"] = data["id"]
		ex["name"] = data["name"]
		ex["authenticationToken"] = data["authenticationToken"]
		ex["authorizedUserIds"] = data["authorizedUserIds"]
		ex["metadata"] = data["metadata"]
		ex["ext"] = data["ext"]

		#print(ex)
		log.logger.info(ex)
		tenants.insert(ex)
		ex.pop("_id")
		return jsonify({'result':ex,'code':200})
	else:
		return jsonify({'result':ex,'code':403})
		
#创建新租户
def tenant_put(mongo,data):
	tenants = mongo.db.tenants
	date = datetime.datetime.now()
	ex = json.loads(exp)
	tenantId = data["id"]
	res = tenants.find_one({"id":tenantId})
	if res != None:
		tenants.remove({"id":tenantId})
		res["createdDate"] = date.strftime("%Y-%m-%d %H:%M:%S")
		res["createdBy"] = "admin"
		#ex["id"] = data["id"]
		res["name"] = data["name"]
		res["authenticationToken"] = data["authenticationToken"]
		res["authorizedUserIds"] = data["authorizedUserIds"]
		res["metadata"] = data["metadata"]
		ex["ext"] = data["ext"]

		#print(res)
		log.logger.info(res)
		tenants.insert(res)
		res.pop("_id")
		return jsonify({'result':res,'code':200})
	else:
		return jsonify({'result': res,'code':403})

def tenant_del(mongo,tenantId):
	tenants = mongo.db.tenants
	ex = json.loads(exp)
	res = tenants.find_one({"id":tenantId})
	if res == None:
		return jsonify({'result': ex,'code':404})
	else:
		tenants.remove({"id":tenantId})
		res.pop("_id")
		print(res)
		return jsonify({'result':res,'code':200})


