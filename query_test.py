# Test script to test response from app. 

import json
import requests
import os

REG_ROOT = 'http://localhost:8081'
AUTH_ROOT = 'http://localhost:8091' 
ZIP_FILE = '12345.zip'

def print_response(r):
    print(r.headers)
    print(r.links)
    print(r.encoding)
    print(r.status_code)
    print('Size = %s' % len(r.content))
    print('Response Data = %s' % r.content)

def register(root_url, zip_file):
    url = root_url + '/registrationprocessor/v1/packetreceiver/registrationpackets'
    files = {'file' : (zip_file, open(zip_file, 'rb'))}
    r = requests.post(url, files = files) 
    print_response(r)

def auth(root_url):
    url = root_url + '/v1/authmanager/authenticate/useridPwd' 
    j = {
	    "id": "mosip.io.userId.pwd",
        "metadata" : {},
	    "version":"1.0",	
	    "requesttime":"2019-06-18T10:15:30.768Z",
	    "request": {
            "appId" : "registrationprocessor",
		    "userName": "110001",
		    "password": "mosip"
        }
	}
    r = requests.post(url, json = j)
    print_response(r)
  

if __name__=='__main__':
    #register(REG_ROOT, ZIP_FILE)
    auth(AUTH_ROOT)

