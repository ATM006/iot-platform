#! /usr/bin/python3

import paho.mqtt.client as mqtt
import log,json,devaccess


class MyMQTTClass(mqtt.Client):
    
	def on_connect(self, mqttc, obj, flags, rc):
		print("rc: "+str(rc))

	def on_message(self, mqttc, obj, msg):
		log.logger.info("call : on_message(self, mqttc, obj, msg)")
		data = json.loads(msg.payload.decode("utf-8"))
		log.logger.info(data["eventType"])
		if data["eventType"] == "RegisterDevice":
			devaccess.register_device(data)
		elif data["eventType"] == "DevicesData":
			devaccess.device_data(data)
		elif data["eventType"] == "DeviceAlert":
			devaccess.device_alert(data)
		elif data["eventType"] == "Acknowledge":
			devaccess.acknowledge(data)

		log.logger.info(data)

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


