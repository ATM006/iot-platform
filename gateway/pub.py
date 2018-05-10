# import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time


HOST = "127.0.0.1"
PORT = 1883

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test")

def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode("utf-8"))



def pub_loop(topic,data):
	while True:
		publish.single(topic,data, qos = 1,hostname=HOST,port=PORT, client_id=client_id)
		time.sleep(10)

if __name__ == '__main__':
	client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
	
	topic = "/iot/input/json"
	#data = '{"led":"true"}'
	
	data = '{\
"eventType":"UserCommand",\
"siteToken":"testtoken",\
"eventDate":"xx",\
"receivedDate":"xx",\
"hardwareId":"test1234560z",\
"metadata":{"xyx":"zzz"},\
"eventbody":[]\
}'

	pub_loop(topic,data)
