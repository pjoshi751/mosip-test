import json
import requests
import os
from config import *

def prereg_send_application(prereg_root, json_file):
    url = prereg_root + '/preregistration/v1/applications'
    j = open(json_file, 'rt').read()
    r = requests.post(url, json=j)
    return r 

def prereg_send_otp():
     url = PREREG_LOGIN_ROOT + '/preregistration/v1/login/sendOtp' 
     j = {
         "id": "mosip.pre-registration.login.sendotp",
         "version": "1.0",
         "requesttime": "2019-08-27T14:00:47.605Z",
         "request": {
             "userId": "bonfiley@gmail.com"
         }
     }

     r = requests.post(url, json=j)
     return r

