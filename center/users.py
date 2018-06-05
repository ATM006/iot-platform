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
"ext":{},\
"metadata": {}\
}'

def te():
	print ("13089u74\n")


def user_get(mongo,name):
	users = mongo.db.users
	ex = json.loads(exp)
	res = users.find_one({"username":name})
	if res == None:
		return jsonify({'result': ex,'code':404})
	else:
		res.pop("_id")
		print(res)
		return jsonify({'result':res,'code':200})


def user_get_all(mongo):
	users = mongo.db.users
	u = users.find()
	out = []
	for item in u:
		item.pop("_id")
		print(item)
		out.append(item)

	return jsonify({'result':out,'code':200})


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
		ex["ext"] = data["ext"]

		print(ex)
		users.insert(ex)
		ex.pop("_id")
		return jsonify({'result':ex,'code':200})
	else:
		return jsonify({'result': ex,'code':403})

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
		res["ext"] = data["ext"]
		res["metadata"] = data["metadata"]
		#print(res)
		log.logger.info(res)
		users.insert(res)
		res.pop("_id")
		return jsonify({'result':res,'code':200})
	else:
		return jsonify({'result': ex,'code':403})


def user_del(mongo,name):
	users = mongo.db.users
	ex = json.loads(exp)
	res = users.find_one({"username":name})
	if res == None:
		return jsonify({'result': ex,'code':404})
	else:
		users.remove({"username":name})
		res.pop("_id")
		print(res)
		return jsonify({'result':res,'code':200})


