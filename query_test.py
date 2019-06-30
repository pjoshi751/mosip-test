# Test script to test response from app. 

import json
import requests
import os

REG_ROOT = 'http://localhost:8081'
REG_STATUS_ROOT = 'http://localhost:8083'
AUTH_ROOT = 'http://localhost:8091' 
CRYPTOMANAGER_ROOT = 'http://localhost:8087'
KEYMANAGER_ROOT = 'http://localhost:8188'
REG_ID = '10003100240000120190531035514'
CLIENTID = '10011'

ZIP_FILE = 'qa/%s.zip' % REG_ID
TIMESTAMP = "2019-02-14T12:40:59.768Z"

def print_response(r):
    print(r.headers)
    print(r.links)
    print(r.encoding)
    print(r.status_code)
    print('Size = %s' % len(r.content))
    print('Response Data = %s' % r.content)

def get_token(response):
    cookies = response.headers['Set-Cookie'].split(';')
    for cookie in cookies:
        key = cookie.split('=')[0]
        value = cookie.split('=')[1]
        if key == 'Authorization':
            return value 

    return None
 
def register(token, reg_root, auth_root, zip_file):
    url = reg_root + '/registrationprocessor/v1/packetreceiver/registrationpackets'
    files = {'file' : (zip_file, open(zip_file, 'rb'))}
    cookies = {'Authorization' : token}
    r = requests.post(url, files = files, cookies=cookies) 
    return r

def register_sync(token, url_root):
    url = url_root + '/registrationprocessor/v1/registrationstatus/sync'
    headers = {'Center-Machine-RefId': CLIENTID, 
               'timestamp': TIMESTAMP}
    cookies = {'Authorization' : token}
    j = {
        "id": "mosip.registration.sync",
        "version": "1.0",
        "requesttime": TIMESTAMP, 
        "request": [{
            "registrationId": REG_ID, 
            "registrationType": "NEW",
            "packetHashValue": "63a77e01bb7488e8b9674d2b4999c906bece3feb3a3fd9137794eb5dbbc3d217",
            "packetSize": 448062,
            "supervisorStatus": "APPROVED",
            "supervisorComment": "Approved, all good",
            "langCode": "eng",
            "optionalValues": [{
                "key": "CNIE",
                "value": "122223456"
            }]
        }]      
    }
    
    r = requests.post(url, json = j, headers=headers, cookies=cookies) 

    return r

def auth(root_url):
    url = root_url + '/v1/authmanager/authenticate/useridPwd' 
    j = {
	    "id": "mosip.io.userId.pwd",
        "metadata" : {},
	    "version":"1.0",	
	    "requesttime": TIMESTAMP,
	    "request": {
            "appId" : "registrationprocessor",
		    "userName": "registration_admin",
		    "password": "mosip"
        }
	}
    r = requests.post(url, json = j)
    return r
  
def validate_token(token, root_url):
    url = root_url + '/v1/authmanager/authorize/validateToken'
    cookies = {'Authorization' : token}
    r = requests.post(url, cookies=cookies) 
    return r

def encrypt(data, token, root_url):  # String or binary
    url = root_url + '/v1/cryptomanager/encrypt'
    cookies = {'Authorization' : token}
    r = requests.post(url, json = data, cookies=cookies) 
    return r 

if __name__=='__main__':
    r = auth(AUTH_ROOT)
    token = get_token(r)
    r = validate_token(token, AUTH_ROOT)
    #r = register_sync(token, REG_STATUS_ROOT)
    #r = register(token, REG_ROOT, AUTH_ROOT, ZIP_FILE)
    data = {
        "id": "TST",
        "version": "1.0",
        "metadata": {},
        "requesttimeStamp": "2018-11-10T06:12:52.994Z",
      	"request": {
      		"applicationId": "REGISTRATION",
      		"data": "Hello World",
      		"referenceId": "REF01",
      		"salt": None,
      		"timeStamp": "2018-11-10T06:12:52.994Z"
      	}	  
    }
    r = encrypt(data, token, CRYPTOMANAGER_ROOT)
    print_response(r)
    exit(0) 

