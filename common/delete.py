
import requests

url = 'http://127.0.0.1:5120/iot/spi/devices/test123456'

r = requests.delete("http://127.0.0.1:5120/iot/spi/devices/test123456")
print(r.text)


