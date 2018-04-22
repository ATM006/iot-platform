#!/usr/bin/python3.5

from flask import Flask
from flask import request,jsonify
from flask_pymongo import PyMongo
import json,uuid,datetime


exp = '{\
"createdDate":"",\
"createdBy":"",\
"id":"",\
"name":"",\
"authenticationToken":"",\
"authorizedUserIds":{},\
"metadata":{}\
}'



def tenant_get(mongo,tenantId):
	tenants = mongo.db.tenants
	res = tenants.find_one({"id":tenantId})
	if res == None:
		return '{"tenant":"not exist!"}'
	else:
		res.pop("_id")
		print(res)
		return jsonify({'result':res})


def tenant_get_all(mongo):
	tenants = mongo.db.tenants
	t = tenants.find()
	out = []
	for item in t:
		item.pop("_id")
		print(item)
		out.append(item)

	return jsonify({'result':out})


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
		print(ex)
		tenants.insert(ex)
		ex.pop("_id")
		return jsonify({'result':ex})
	else:
		return '{"tenant":"exist"}'
		

def tenant_del(mongo,tenantId):
	tenants = mongo.db.tenants
	res = tenants.find_one({"id":tenantId})
	if res == None:
		return '{"tenant":"not exist"}'
	else:
		tenants.remove({"id":tenantId})
		res.pop("_id")
		print(res)
		return jsonify({'result':res})


