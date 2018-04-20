#!/usr/bin/python3.5

from flask import Flask
from flask import request,jsonify
from flask_pymongo import PyMongo
import json,uuid,datetime


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
	res = users.find_one({"username":name})
	if res == None:
		return '{"user":"not exist!"}'
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
		return '{"user":"exist"}'
		

def user_del(mongo,name):
	users = mongo.db.users
	res = users.find_one({"username":name})
	if res == None:
		return '{"user":"not exist"}'
	else:
		users.remove({"username":name})
		res.pop("_id")
		print(res)
		return jsonify({'result':res})


