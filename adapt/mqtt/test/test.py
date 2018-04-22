import mqttclass

mqttc = mqttclass.MyMQTTClass()
rc = mqttc.run()
 
print("rc: "+str(rc))

