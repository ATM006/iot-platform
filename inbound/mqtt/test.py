
import mqttclass
import log

mqttc = mqttclass.MyMQTTClass()
rc = mqttc.run()
 
print("rc: "+str(rc))
log.logger.info("rc: "+str(rc))

