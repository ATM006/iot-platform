#! /usr/bin/python

import requests

url = "http://127.0.0.1:5000/api/led"
data = '{"led":"true"}'


def my_post(url,data):
	r = requests.post(url,data)
	print(r.text)


if __name__ == '__main__':
	my_post(url,data)

