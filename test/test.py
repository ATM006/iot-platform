#查询发布会接口测试代码
import requests

url = "http://127.0.0.1:5120/iot/spi/users"
r = requests.get(url)
result = r.json()

print(result)
