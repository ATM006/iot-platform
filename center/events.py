#!/usr/bin/python3.5

from flask import Flask
from flask import request,jsonify
from flask_pymongo import PyMongo
import json,uuid,datetime

exp = '{\
"eventType":"",\
"siteToken":"",\
"eventDate":"",\
"receivedDate":"",\
"hardwareId":"",\
"metadata":{},\
"eventbody":[]\
}'


<<<<<<< HEAD
=======
#MongoDB服务接口实现
'''
>>>>>>> origin/dev
def event_get(mongo,hardwareId):
    
    events = mongo.db.events
    devices = mongo.db.devices
    res = devices.find()
	#res = events.find_one()
    
    if res == None:
        return '{"event":"not exist"}'
    else:
        e = events.find({"hardwareId":hardwareId})
        out = []
        
        for item in e:
            item.pop("_id")
            print(item)
            out.append(item)

        return jsonify({'result':out})




def event_post(mongo,data,hardwareId):
	events = mongo.db.events
	devices = mongo.db.devices
	date = datetime.datetime.now()
	ex = json.loads(exp)
	hardwareId = data["hardwareId"]
	if devices.find_one({"hardwareId":hardwareId}) == None:
		return '{"hardwareId":"not exist"}'
	else:
		ex["eventType"] = data["eventType"]
		ex["siteToken"] = data["siteToken"]
		ex["eventDate"] = date.strftime("%Y-%m-%d %H:%M:%S")
		ex["receivedDate"] = date.strftime("%Y-%m-%d %H:%M:%S")
		ex["hardwareId"] = hardwareId
		ex["metadata"] = data["metadata"]
		ex["eventbody"] = data["eventbody"]

		print(ex)
		events.insert(ex)
		ex.pop("_id")
		return jsonify({'result':ex})

'''

def event_get(mongo,hardwareId):
	events = mongo.db.events
	devices = mongo.db.devices
	res = devices.find()
	#res = events.find_one()
	if res == None:
		return '{"event":"not exist"}'
	else:
		e = events.find({"hardwareId":hardwareId})
		out = []
		for item in e:
			item.pop("_id")
			print(item)
			out.append(item)

		return jsonify({'result':out})




def event_post(mongo,data,hardwareId):
	events = mongo.db.events
	devices = mongo.db.devices
	date = datetime.datetime.now()
	ex = json.loads(exp)
	hardwareId = data["hardwareId"]
	if devices.find_one({"hardwareId":hardwareId}) == None:
		return '{"hardwareId":"not exist"}'
	else:
		ex["eventType"] = data["eventType"]
		ex["siteToken"] = data["siteToken"]
		ex["eventDate"] = date.strftime("%Y-%m-%d %H:%M:%S")
		ex["receivedDate"] = date.strftime("%Y-%m-%d %H:%M:%S")
		ex["hardwareId"] = hardwareId
		ex["metadata"] = data["metadata"]
		ex["eventbody"] = data["eventbody"]

		print(ex)
		events.insert(ex)
		ex.pop("_id")
		return jsonify({'result':ex})

