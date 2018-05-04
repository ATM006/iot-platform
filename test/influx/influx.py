#########################################################################
# File Name: influx.py
# Author   : ATM006
# mail     : 18829897162@163.com
# Time: 2018年05月01日 星期二 10时29分09秒
#########################################################################
#!/usr/bin/python
#-*- coding:utf8 -*-


from influxdb import InfluxDBClient

client = InfluxDBClient('localhost', 8086, 'root', '', '') # 初始化

print(client.get_list_database()) # 显示所有数据库名称

client.create_database('testdb') # 创建数据库

print(client.get_list_database()) # 显示所有数据库名称

#client.drop_database('testdb') # 删除数据库

#print(client.get_list_database()) # 显示所有数据库名称

