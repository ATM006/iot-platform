#stop.sh


ps -ef|grep run-|grep -v grep|awk '{print "kill -9 "$2}'
ps -ef|grep run-|grep -v grep|awk '{print "kill -9 "$2}'|sh

