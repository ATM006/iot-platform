import unittest
import requests

class user_SPI_test(unittest.TestCase):

    def setUp(self):

        self.base_url = "http://127.0.0.1:5120/"

    def test_index_SPI(self):

        r = requests.get(self.base_url)
        r = r.text
        self.assertEqual(r,"The IoT SPI")

    def test_index_SPI2(self):

        r = requests.get(self.base_url)
        r = r.text
        print (r)

if __name__ == '__main__':
     unittest.main()