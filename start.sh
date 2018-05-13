#!/bin/bash

#启动环境
#echo "sudo sh start-env.sh"
#sudo sh start-env.sh
#启动服务
echo "启动服务......"

echo "python center/run-center.py"
python center/run-center.py 


#echo "python process/run-process.py"
#python process/run-process.py 1>x 2>y &

#echo "python console/app.py"
#python console/app.py 1>x 2>y &

#echo "python admin/run.py"
#python admin/run.py 1>x 2>y &

#echo "python devaccess/mqtt/run-devacc.py"
#python devaccess/mqtt/run-devacc.py 1>x 2>y &

