
from pymongo import MongoClient


#conn = MongoClient(host=)

import configparser
import os

conf = configparser.ConfigParser()
conf.read("../conf/connect.conf")

host = conf.get('db','db_host')
port = int(conf.get('db','db_port'))

print(host,port)

client = MongoClient('127.0.0.1',27017)
#print(client)

db = client.iot
leds = db.test_led

leds.insert({"led":"true"})







client.close()
