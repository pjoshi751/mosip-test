
import json
import requests
import os
from config import *

def encrypt(data, token, root_url):  # String or binary
    url = root_url + '/v1/cryptomanager/encrypt'
    cookies = {'Authorization' : token}
    r = requests.post(url, json = data, cookies=cookies) 
    return r 

def get_public_key(token, appid, root_url):
    url = root_url + '/v1/keymanager/publickey/%s?timeStamp=2018-11-10T06:12:52.994Z' % appid 
    #http://localhost:8188/v1/keymanager/publickey/REGISTRATION?timeStamp=2018-12-09T06%3A39%3A03.683Z 
    cookies = {'Authorization' : token}
    r = requests.get(url, cookies=cookies) 
    return r

