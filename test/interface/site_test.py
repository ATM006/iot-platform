import unittest
import requests

class site_SPI_test(unittest.TestCase):

    global test_token

    def setUp(self):
        self.base_url = "http://127.0.0.1:5120/iot/spi/sites"



    #创建区域接口测试
    def test_a_site_post(self):
        global test_token
        data = '{"token":"","name":"test","description":"testsite","metadata" : {},"ext":{}}'
        res = requests.post(self.base_url,data)
        res = res.json()
        self.assertEqual(res['code'],200)
        test_token = res['result']['token']
        print (res)


    # 查看区域列表接口测试
    def test_b_site_get_list(self):
        res = requests.get(self.base_url).json()
        self.assertEqual(res['code'], 200)
        print (res)

    ''' 
    def test_c_site_put(self):
        global test_token
        data = '{"token":'+ test_token+',"name":"test","description":"test","metadata" : {},"ext":{}}'
        res = requests.put(self.base_url + "/" + test_token, data).json()
        self.assertEqual(res['code'], 200)     
        print (res)
    '''

    #查看特定区域接口测试
    def test_d_site_get(self):
        global test_token
        res = requests.get(self.base_url +"/"+test_token).json()
        self.assertEqual(res['code'], 200)
        print (res)

    # 删除区域接口测试
    def test_e_site_delete(self):
        global test_token
        res = requests.delete(self.base_url +"/"+test_token).json()
        self.assertEqual(res['code'], 200)
        print (res)


if __name__ == '__main__':
     unittest.main()