#!/usr/bin/python3
# -*- coding:utf-8 -*-
 
import redis


pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

r = redis.Redis(connection_pool=pool)
r.set("led","true")
print(r.get("led"))


""" 
#r = redis.Redis()
r = redis.Redis(host='127.0.0.1', port=6379)
r.set('foo', 'Bar')
print(r.get('foo'))
"""


