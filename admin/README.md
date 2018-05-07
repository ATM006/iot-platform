/***
  * @file   README.md
  *
  *
  *
  * @author ATM006   <18829897162@163.com>
  * @date   2018-05-04 10:37:18 上午
  *
  */


curl -X GET http://127.0.0.1:8080/iot/api/devices

curl -X GET http://127.0.0.1:8080/iot/api/devices/test123456

curl -X POST http://127.0.0.1:8080/iot/api/users -d '{"username":"atm","hashedPassword":"123456","metadata":{}}'

curl -X PUT http://127.0.0.1:5120/iot/spi/users -d '{"username":"atm","hashedPassword":"1234561","metadata":{}}'


