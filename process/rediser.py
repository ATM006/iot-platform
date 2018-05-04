#!/usr/bin/python3
# -*- coding:utf-8 -*-

import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

redis_pool = redis.Redis(connection_pool=pool)


