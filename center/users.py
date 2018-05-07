#!/usr/bin/python3.5

from flask import Flask
from flask import request,jsonify
from flask_pymongo import PyMongo
import json,uuid,datetime
import log

exp = '{\
"createdDate": "",\
"createdBy": "",\
"username": "",\
"hashedPassword": "",\
"lastLogin": "",\
"status": "",\
"metadata": {}\
}'


def user_get(mongo,name):
	users = mongo.db.users
	ex = json.loads(exp)
	res = users.find_one({"username":name})
	if res == None:
		return jsonify({'result': ex})
	else:
		res.pop("_id")
		print(res)
		return jsonify({'result':res})


def user_get_all(mongo):
	users = mongo.db.users
	u = users.find()
	out = []
	for item in u:
		item.pop("_id")
		print(item)
		out.append(item)

	return jsonify({'result':out})


def user_post(mongo,data):
	users = mongo.db.users
	date = datetime.datetime.now()
	ex = json.loads(exp)
	name = data["username"]
	if users.find_one({"username":name}) == None:
		ex["createdDate"] = date.strftime("%Y-%m-%d %H:%M:%S")
		ex["createdBy"] = "admin"
		ex["username"] = data["username"]
		ex["hashedPassword"] = data["hashedPassword"]
		ex["lastLogin"] = date.strftime("%Y-%m-%d %H:%M:%S")
		ex["status"] = True
		ex["metadata"] = data["metadata"]
		print(ex)
		users.insert(ex)
		ex.pop("_id")
		return jsonify({'result':ex})
	else:
		return jsonify({'result': ex})

#创建新用户
def user_put(mongo,data):
	log.logger.info("call : user_post(mongo,data)")
	users = mongo.db.users
	date = datetime.datetime.now()
	ex = json.loads(exp)
	name = data["username"]
	res = users.find_one({"username":name})
	if res != None:
		users.remove({"username":name})
		res["createdDate"] = date.strftime("%Y-%m-%d %H:%M:%S")
		res["createdBy"] = "admin"
		res["username"] = data["username"]
		res["hashedPassword"] = data["hashedPassword"]
		res["lastLogin"] = date.strftime("%Y-%m-%d %H:%M:%S")
		res["status"] = True
		res["metadata"] = data["metadata"]
		#print(res)
		log.logger.info(res)
		users.insert(res)
		res.pop("_id")
		return jsonify({'result':res})
	else:
		return jsonify({'result': ex})


def user_del(mongo,name):
	users = mongo.db.users
	ex = json.loads(exp)
	res = users.find_one({"username":name})
	if res == None:
		return jsonify({'result': ex})
	else:
		users.remove({"username":name})
		res.pop("_id")
		print(res)
		return jsonify({'result':res})


