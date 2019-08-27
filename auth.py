
import json
import requests
import os
from config import *

  
def validate_token(token, root_url):
    url = root_url + '/v1/authmanager/authorize/validateToken'
    cookies = {'Authorization' : token}
    r = requests.post(url, cookies=cookies) 
    return r


def send_otp(email):
    j = {
       "id": "string",
       "metadata": {},
       "request": {
           "appId": "ida",
            "otpChannel": [
                "email"
         ],
           "context":"auth-otp",
           "templateVariables":{"UIN":"2530192395"},
           "userId": "2530192395",
           "useridtype": "UIN"
       },
       "requesttime": "2019-04-29T07:01:24.692Z",
       "version": "string"
    }
