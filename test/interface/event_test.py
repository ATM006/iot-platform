import unittest
import requests

class event_SPI_test(unittest.TestCase):

    test_hardwareId = 'test1234560z'

    def setUp(self):
        self.base_url = "http://127.0.0.1:5120/iot/spi/devices"



    #存储用户命令接口测试
    def test_a_usercommand_post(self):
        data = '{"eventType":"UserCommands","siteToken":"testtoken","hardwareId":"test1234560z","metadata":{},"eventbody":{},"ext":{"test":"test"}}'
        res = requests.post(self.base_url+"/"+self.test_hardwareId+"/events/UserCommands",data)
        res = res.json()
        self.assertEqual(res['code'],200)
        print (res)


    #查看用户历史操作接口测试#
    def test_b_usercommand_get_(self):
        res = requests.get(self.base_url+"/"+self.test_hardwareId+"/events/UserCommands").json()
        self.assertEqual(res['code'], 200)
        print (res)


    #存储设备数据接口测试
    def test_a_devicedata_post(self):
        data = '{"eventType":"DevicesData","siteToken":"testtoken","hardwareId":"test1234560z","metadata":{},"eventbody":{},"ext":{"test":"test"}}'
        res = requests.post(self.base_url+"/"+self.test_hardwareId+"/events/DevicesData",data)
        res = res.json()
        self.assertEqual(res['code'],200)
        print (res)


    #查看设备历史数据接口测试#
    def test_b_devicedata_get_(self):
        res = requests.get(self.base_url+"/"+self.test_hardwareId+"/events/DevicesData").json()
        self.assertEqual(res['code'], 200)
        print (res)

if __name__ == '__main__':
     unittest.main()