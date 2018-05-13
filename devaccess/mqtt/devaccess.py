#! /usr/bin/python3

import requests,log,json,datetime
from flask import request,jsonify
import paho.mqtt.publish as publish
import time

url = 'http://127.0.0.1:5211/iot/api/devices/test1234560/events/DevicesData/'
urlt = 'http://127.0.0.1:5211/iot/api/devices/'

#curl -X POST  http://127.0.0.1:5000/iot/api/devices -d '{"hardwareId":"test123456","siteToken":"","comments":"","metadata": {}}'

reg = 'http://127.0.0.1:5122/iot/api/devices'

exp = '{\
"createdDate": "",\
"createdBy": "",\
"hardwareId": "",\
"siteToken":"",\
"comments":"",\
"metadata": {}\
}'

def register_device(data):
    log.logger.info("call : register_device(data)")
    # 注册设备
    log.logger.info("注册设备")
    date = datetime.datetime.now()
    ex = json.loads(exp)
    ex["createdDate"] = date.strftime("%Y-%m-%d %H:%M:%S")
    ex["createdBy"] = 'auto'
    ex["hardwareId"] = data["hardwareId"]
    ex["siteToken"] = data["siteToken"]
    ex["comments"] = ''
    ex["metadata"] = ''
    res = requests.post(reg, json.dumps(ex)).json()
    log.logger.info(res)

def device_data(data):
    log.logger.info("call : device_data(data)")
    #发布数据
    data_publish(data)
    res = requests.post(urlt + data["hardwareId"] + "/events/",json.dumps(data)).json()
    print(res)
    if res["result"]["hardwareId"] == '':
        #注册设备
        register_device(data)
        requests.post(urlt + data["hardwareId"] + "/events/", json.dumps(data)).json()





def device_alert(data):
    log.logger.info("call : device_alert(data)")
    pass

def acknowledge(data):
    log.logger.info("call : acknowledge(data)")
    pass



def user_command(data):
    log.logger.info("call : user_command(data)")
    log.logger.info(data)
    requests.post(urlt + data["hardwareId"] + "/events/", json.dumps(data))


def registration_ack(data):
    log.logger.info("call : registration_ack(data)")
    pass


'''发布实时数据'''
topic = "/iot/output/json"
HOST = "127.0.0.1"
PORT = 1883

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test")

def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode("utf-8"))


def data_publish(data):
    log.logger.info("call : data_publish(data)")
    client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    publish.single(topic, json.dumps(data), qos=1, hostname=HOST, port=PORT, client_id=client_id)


