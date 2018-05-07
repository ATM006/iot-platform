#!/usr/bin/python3.5

from flask import Flask
from flask import request,jsonify
#from flask_pymongo import PyMongo
import json

import log

app = Flask(__name__)




def led_get_all(mongo):
	log.logger.info("call led_get_all()")
	li = mongo.db.test_led.find()
	out = []
	for i in li: 
		out.append({'led':i['led']})
	return jsonify({'result':out})


def led_post(mongo,data):
	leds = mongo.db.test_led
	leds.insert(data)
	return "POST led"


def led_put(mongo,data):
	return "led not put\n"