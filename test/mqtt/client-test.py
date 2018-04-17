import paho.mqtt.client as client
import time

#HOST = "127.0.0.1"
HOST = "47.95.254.34"
PORT = 1883

def on_publish(client,userdata,mid):
	print("mid: "+str(mid))



def pub_loop():
	while True:
		data = '{"led":"false"}'
		(rc,mid) = client.publish("test",str(data))
		time.sleep(60)

		data = '{"led":"true"}'
		(rc,mid) = client.publish("test",str(data))
		time.sleep(60)


if __name__ == '__main__':
	client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
	client = client.Client(client_id)
	client.on_publish = on_publish
	client.connect(host=HOST,port=PORT)
	client.loop_start()
	pub_loop()
	
 


