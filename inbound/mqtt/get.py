#! /usr/bin/python
#get.py

import requests

url = "http://127.0.0.1:5000/iot/api/led"

r = requests.get(url)
print(r.text)
