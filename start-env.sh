#########################################################################
# File Name: start-env.sh
# Author   : ATM006
# mail     : 18829897162@163.com
<<<<<<< HEAD
# Time: 2018年05月01日 星期二 11时51分17秒
=======
# Time: 2018年05月04日 星期五 09时26分29秒
>>>>>>> origin/dev
#########################################################################
#!/bin/bash

#启动MongoDB
sudo service mongod restart
#启动Influx
<<<<<<< HEAD
sudo service influxdb restart
#启动hiveMQ

=======
sudo influxd run &
#启动hiveMQ
cd /opt/hivemq-3.0.2/bin/
./run.sh &
>>>>>>> origin/dev

#启动redis
redis-server &
