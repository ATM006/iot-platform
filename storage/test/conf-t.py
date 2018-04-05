
#from pymongo import MongoClient


#conn = MongoClient(host=)

import configparser
import os

conf = configparser.ConfigParser()
conf.read("../conf/connect.conf")

host = conf.get('db','db_host')

print(host)
