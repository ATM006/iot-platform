#########################################################################
# File Name: data.py
# Author   : ATM006
# mail     : 18829897162@163.com
# Time: 2018年05月04日 星期五 10时07分38秒
#########################################################################
#!/usr/bin/python
#-*- coding:utf8 -*-


from flask import request,jsonify
import log,rediser
import requests

urlt = 'http://127.0.0.1:5120/iot/spi/devices/'


def data_post_process(hardwareId,data):
    log.logger.info("call : data_post_process()")
    rpool = rediser.redis_pool
    rpool.set(hardwareId+'data', data)
    res = requests.post(urlt + hardwareId + "/events/", request.get_data())
    log.logger.info(res.text)
    res = res.json()
    return jsonify(res)
    #return "call data_post_process()\n"


def data_get_process(hardwareId):
    log.logger.info("call : data_get_process()")
    rpool = rediser.redis_pool
    res = rpool.get(hardwareId+'data')
    if res != None:
        res = res.decode('utf-8')
        return jsonify({'result': res})
    else:
        res = requests.get(urlt + hardwareId + "/events/")
        res = res.json()
        return jsonify({'result': res})





