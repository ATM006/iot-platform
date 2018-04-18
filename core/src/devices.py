#!/usr/bin/python3.5

from flask import Flask
from flask import request,jsonify
from flask_pymongo import PyMongo
import json



def device_get(mongo):
	return "GET devices"


def device_post(mongo,data):
	return "POST devices"

def deviec_del(mongo):
	
	return "DELETE devices"


