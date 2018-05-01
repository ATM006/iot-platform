#########################################################################
# File Name: start-env.sh
# Author   : ATM006
# mail     : 18829897162@163.com
# Time: 2018年05月01日 星期二 11时51分17秒
#########################################################################
#!/bin/bash

#启动MongoDB
sudo service mongod restart
#启动Influx
sudo service influxdb restart
#启动hiveMQ


#启动redis
redis-server &
