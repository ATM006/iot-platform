import unittest
import requests

class user_SPI_test(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:5120/iot/spi/users"

    # 删除用户接口测试
    def test__e_user_delete(self):
        res = requests.delete(self.base_url + "/unit-test").json()
        self.assertEqual(res['code'], 200)
        print (res)


    # 查看特定用户接口测试
    def test_d_user_get(self):
        res = requests.get(self.base_url + "/unit-test").json()
        self.assertEqual(res['code'], 200)
        print (res)

    # 更新用户接口测试
    def test_c_user_put(self):
        data = '{"username":"unit-test","hashedPassword":"123456","metadata":{},"ext":{}}'
        res = requests.put(self.base_url, data).json()
        self.assertEqual(res['code'], 200)
        print (res)


    #创建用户接口测试
    def test_a_user_post(self):
        data = '{"username":"unit-test","hashedPassword":"123456","metadata":{},"ext":{}}'
        res = requests.post(self.base_url,data)
        res = res.json()
        self.assertEqual(res['code'],200)
        print (res)


    # 查看用户列表接口测试
    def test_b_user_get_list(self):
        res = requests.get(self.base_url).json()
        self.assertEqual(res['code'], 200)
        print (res)






if __name__ == '__main__':
     unittest.main()