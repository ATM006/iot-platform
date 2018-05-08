
	设备接入层设计


MQTT协议设计

1、数据订阅：
1）、检查设备有没有注册？如果已经注册则，接受数据；否则，发起自注册流程
2）、是否注册判断：


2、新设备自注册：接入层发起设备注册请求，注册设备；接受数据


接口协议：
1、MQTT主题：/iot/input/json
2、接入格式：
data = '{\ 
"eventType":"DevicesData",\		#事件类型：必填（目前只支持DevicesData）
"siteToken":"testtoken",\		#站点token（网关填写）：必填
"eventDate":"xx",\
"receivedDate":"xx",\			
"hardwareId":"test1234560x",\	#设备ID：必填
"metadata":{"xyx":"zzz"},\
"eventbody":[]\					#数据必填
}'

#件类型：RegisterDevice、DevicesData、DeviceAlert、cknowledge
注:填 (只支持DevicesData)


3、订阅格式
见: iot/publish/README.md



