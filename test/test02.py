import unittest
import requests

class SPITest(unittest.TestCase):

    def setUp(self):

        self.base_url = "http://127.0.0.1:5120/iot/spi/users"

    def test_user_SPI(self):

        r = requests.get(self.base_url)
        result = r.json()
        self.assertEqual(result['code'], 200)



if __name__ == '__main__':
     unittest.main()