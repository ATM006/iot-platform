#!/usr/bin/python3

import requests,json
import log

url = 'http://127.0.0.1:5120/iot/spi/'

def authority_user(name,password):
    log.logger.info("call : authority_user(name,password)")
    res = requests.get(url + "users/" + name).json()
    print(res)
    if res["result"]["username"] == name and res["result"]["hashedPassword"] == password:
    #if True:
        return True
    else:
        return False

