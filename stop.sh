#stop.sh


#ps -ef|grep run-|grep -v grep|awk '{print "kill -9 "$2}'
echo ">>>"
echo ">>>: The IoT Service platform stopping ..."
ps -ef|grep run-|grep -v grep|awk '{print "kill -9 "$2}'|sh
