#!/usr/bin/python3.5

from flask import Flask
from flask import request,jsonify
from flask_pymongo import PyMongo
import json



def user_get(mongo):
	return "GET users"


def user_post(mongo,data):
	return "POST users"

def user_del(mongo):
	
	return "DELETE users"


