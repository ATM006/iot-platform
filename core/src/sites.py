#!/usr/bin/python3.5

from flask import Flask
from flask import request,jsonify
from flask_pymongo import PyMongo
import json



def site_get(mongo):
	li = mongo.db.test_led.find()
	out = []
	for i in li: 
		out.append({'led':i['led']})
	return jsonify({'result':out})


def site_post(mongo,data):
	sites = mongo.db.sites
	sites.insert(data)
	return "POST sites"

def site_del(mongo):
	
	return "DELETE sites"

