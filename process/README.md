


curl -X POST http://127.0.0.1:5121/iot/api/devices/test1234560/events/ -d '{"eventType":"DevicesData","siteToken":"testtoken","hardwareId":"test123456","metadata":{},"eventbody":{}}'


curl -X GET http://127.0.0.1:5121/iot/api/devices/test1234560/events/DevicesData/


curl -X POST http://127.0.0.1:5121/iot/api/devices/test1234560/events/ -d '{"eventType":"UserCommands","siteToken":"testtoken","hardwareId":"test1234560","metadata":{"test":"456"},"eventbody":{}}'

curl -X GET http://127.0.0.1:5121/iot/api/devices/test1234560/events/UserCommands/
