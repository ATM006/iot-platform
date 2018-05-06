#########################################################################
# File Name: start-env.sh
# Author   : ATM006
# mail     : 18829897162@163.com
# Time: 2018年05月04日 星期五 09时26分29秒
#########################################################################
#!/bin/bash

#启动MongoDB
sudo service mongod restart
#启动Influx
sudo influxd run &
#启动hiveMQ
cd /opt/hivemq-3.0.2/bin/
./run.sh &

#启动redis
redis-server &
