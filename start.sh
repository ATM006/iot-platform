#!/bin/bash

#启动环境
#echo "sudo sh start-env.sh"
#sudo sh start-env.sh
#启动服务

echo "启动服务......"

echo "启动【Center Service】：gunicorn -w 2 -b 127.0.0.1:5120 run-center:app 1>x 2>y &"
cd center/
gunicorn -w 2 -b 127.0.0.1:5120 run-center:app 1>x 2>y &
cd -

echo "启动【Process Service】：gunicorn -w 2 -b 127.0.0.1:5211 run-process:app 1>x 2>y &"
cd process/
gunicorn -w 2 -b 127.0.0.1:5211 run-process:app 1>x 2>y &
cd -

echo "启动【Admin Service】：gunicorn -w 2 -b 127.0.0.1:5122 run-admin:app 1>x 2>y &"
cd admin/
gunicorn -w 2 -b 127.0.0.1:5122 run-admin:app 1>x 2>y &
cd -


echo "启动【Console Service】：python3.5 run-app.py 1>x 2>y &"
cd console/
python3.5 run-app.py 1>x 2>y &
cd -


echo "启动【DevAccess Service】：python3.5 run-devacc.py 1>x 2>y &"
cd devaccess/mqtt/
python3.5 run-devacc.py 1>x 2>y &
cd ../../


