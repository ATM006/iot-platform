import unittest
import requests

class tenant_SPI_test(unittest.TestCase):


    def setUp(self):
        self.base_url = "http://127.0.0.1:5120/iot/spi/tenants"



    #创建租户接口测试
    def test_a_tenant_post(self):
        data = '{"id":"unit-test","name":"testtenant","authenticationToken":"","authorizedUserIds":["admin"],"metadata": {},"ext":{}}'
        res = requests.post(self.base_url,data)
        res = res.json()
        self.assertEqual(res['code'],200)
        print (res)


    # 查看租户列表接口测试
    def test_b_tenant_get_list(self):
        res = requests.get(self.base_url).json()
        self.assertEqual(res['code'], 200)
        print (res)

    # 更新租户接口测试
    def test_c_tenant_put(self):
        data = '{"id":"unit-test","name":"test 123","authenticationToken":"","authorizedUserIds":["admin"],"metadata": {},"ext":{}}'
        res = requests.put(self.base_url, data).json()
        self.assertEqual(res['code'], 200)
        #self.assertEqual(res['result']['description'],'test 123')
        print (res)

    # 查看特定租户接口测试
    def test_d_tenant_get(self):
        res = requests.get(self.base_url + "/unit-test").json()
        self.assertEqual(res['code'], 200)
        print (res)

    # 删除租户接口测试
    def test_e_tenant_delete(self):
        res = requests.delete(self.base_url + "/unit-test").json()
        self.assertEqual(res['code'], 200)
        print (res)


if __name__ == '__main__':
     unittest.main()