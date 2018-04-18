#!/usr/bin/python3.5

from flask import Flask
from flask import request,jsonify
from flask_pymongo import PyMongo
import json



def event_get(mongo):
	return "GET events"


def event_post(mongo,data):
	return "POST events"



