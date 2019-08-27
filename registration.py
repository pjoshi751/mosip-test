import json
import requests
import os
from config import *

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

def reg_auth(root_url):
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
