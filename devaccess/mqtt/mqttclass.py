#! /usr/bin/python3

import paho.mqtt.client as mqtt
import log,json,devaccess


class MyMQTTClass(mqtt.Client):
    
	def on_connect(self, mqttc, obj, flags, rc):
		print("rc: "+str(rc))

	def on_message(self, mqttc, obj, msg):
		#print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
		#log.logger.info()
		data = json.loads(msg.payload.decode("utf-8"))
		if data["type"] == "RegisterDevice":
			print("1")
			devaccess.register_device()
		elif data["type"] == "DeviceData":
			print("2")
			devaccess.device_data()
		elif data["type"] == "DeviceAlert":
			print("3")
			devaccess.device_alert()
		elif data["type"] == "Acknowledge":
			print("4")
			devaccess.acknowledge()
		print(data)

	def on_publish(self, mqttc, obj, mid):
		print("mid: "+str(mid))
		#log.logger.info

	def on_subscribe(self, mqttc, obj, mid, granted_qos):
		print("Subscribed: "+str(mid)+" "+str(granted_qos))
		#log.logger.info

	def on_log(self, mqttc, obj, level, string):
		print(string)
		#log.logger.info

	def run(self):
		self.connect("127.0.0.1", 1883, 60)
		#log.logger.info
		#self.subscribe("test", 0)
		self.subscribe("/iot/input/json", 0)

		rc = 0
		while rc == 0:
			rc = self.loop()
		return rc


