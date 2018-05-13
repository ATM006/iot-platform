#! /usr/bin/python3

import paho.mqtt.publish as publish
import log
import time,json

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
