import unittest
import requests

class device_SPI_test(unittest.TestCase):


    def setUp(self):
        self.base_url = "http://127.0.0.1:5120/iot/spi/devices"



    #创建设备接口测试
    def test_a_device_post(self):
        data = '{"hardwareId":"unit-test","siteToken":"","comments":"","metadata":{},"ext":{}}'
        res = requests.post(self.base_url,data)
        res = res.json()
        self.assertEqual(res['code'],200)
        print (res)


    # 查看设备列表接口测试
    def test_b_device_get_list(self):
        res = requests.get(self.base_url+"?type=all").json()
        self.assertEqual(res['code'], 200)
        print (res)

    # 更新设备接口测试
    def test_c_device_put(self):
        data = '{"hardwareId":"test123456","siteToken":"","comments":"","metadata":{},"ext":{}}'
        res = requests.put(self.base_url, data).json()
        self.assertEqual(res['code'], 200)
        #self.assertEqual(res['result']['description'],'test 123')
        print (res)

    # 查看特定设备接口测试
    def test_d_device_get(self):
        res = requests.get(self.base_url + "/unit-test").json()
        self.assertEqual(res['code'], 200)
        print (res)

    # 删除设备接口测试
    def test_e_device_delete(self):
        res = requests.delete(self.base_url + "/unit-test").json()
        self.assertEqual(res['code'], 200)
        print (res)


if __name__ == '__main__':
     unittest.main()