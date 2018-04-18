#!/usr/bin/python3.5

from flask import Flask
from flask import request,jsonify
from flask_pymongo import PyMongo
import json
import uuid


def site_get(mongo):
	return "GET sites"


def site_post(mongo,data):
	sites = mongo.db.sites
	token =data["token"]
	if token == '':
		data["token"] = uuid.uuid1()
	#print(data)
	sites.insert(data)
	return "POST sites"

def site_del(mongo):
	
	return "DELETE sites"


