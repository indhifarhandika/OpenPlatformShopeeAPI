#!/usr/bin/env python3
# encoding: utf-8 
import hmac
import time
import requests
import hashlib
import json

"""
code by : indhifarhandika
"""

__author__ = "indhifarhandika"
__email__ = "indhifarhandika@gmail.com"
__status__ = "planning"


class Shopee():
    def __init__(self):
        self.host = "https://partner.shopeemobile.com"

    # Get Access Token
    def get_token_shop_level(self, code, partner_id, partner_key, shop_id):
        timestamp           = int(time.time())
        body                = {
            "code"      : code,
            "shop_id"   : shop_id,
            "partner_id": partner_id
        }
        path                = "/api/v2/auth/token/get"
        base_string         = f"{partner_id}{path}{timestamp}"
        sign                = hmac.new(partner_key, msg = base_string.encode('utf-8'), digestmod = hashlib.sha256).hexdigest()
        url                 = f"{self.host}{path}?partner_id={partner_id}&timestamp={timestamp}&sign={sign}"
        headers             = { "Content-Type": "application/json" }
        resp                = requests.post(url, json=body, headers=headers)
        ret                 = json.loads(resp.content)
        access_token        = ret.get("access_token")
        new_refresh_token   = ret.get("refresh_token")

        result = {
            'access_token': access_token,
            'new_refresh_token': new_refresh_token,
        }

        return result 

    def get_token_account_level(self, code, partner_id, partner_key, main_account_id):
        timestamp           = int(time.time())
        body                = {
            "code"              : code,
            "main_account_id"   : main_account_id,
            "partner_id"        : partner_id
        }
        path                = "/api/v2/auth/token/get"
        base_string         = f"{partner_id}{path}{timestamp}"
        sign                = hmac.new(partner_key, msg = base_string.encode('utf-8'), digestmod = hashlib.sha256).hexdigest()
        url                 = f"{self.host}{path}?partner_id={partner_id}&timestamp={timestamp}&sign={sign}"
        headers             = { "Content-Type": "application/json"}
        resp                = requests.post(url, json=body, headers=headers)
        ret                 = json.loads(resp.content)
        access_token        = ret.get("access_token")
        new_refresh_token   = ret.get("refresh_token")

        result = {
            'access_token': access_token,
            'new_refresh_token': new_refresh_token,
        }

        return result 

    # Refresh Access Token
    def get_access_token_shop_level(self, refresh_token, partner_id, partner_key, shop_id):
        timestamp           = int(time.time())
        body                = {
            "shop_id"       : shop_id,
            "refresh_token" : refresh_token
        }
        path                = "/api/v2/auth/token/get"
        base_string         = f"{partner_id}{path}{timestamp}"
        sign                = hmac.new(partner_key, msg = base_string.encode('utf-8'), digestmod = hashlib.sha256).hexdigest()
        url                 = f"{self.host}{path}?partner_id={partner_id}&timestamp={timestamp}&sign={sign}"
        headers             = {"Content-Type": "application/json"}
        resp                = requests.post(url, json=body, headers=headers)
        ret                 = json.loads(resp.content)
        access_token        = ret.get("access_token")
        new_refresh_token   = ret.get("refresh_token")
        result = {
            'access_token': access_token,
            'new_refresh_token': new_refresh_token,
        }

        return result

    # Hit API
    def hitApi(self, partner_id, shop_id, partner_key, path, access_token):
        timestamp   = int(time.time())
        base_string = f"{partner_id}{path}{timestamp}{access_token}{shop_id}"
        sign        = hmac.new(partner_key, msg = base_string.encode('utf-8'), digestmod = hashlib.sha256).hexdigest()
        url         = f"{self.host}{path}?partner_id={partner_id}&shop_id={shop_id}&timestamp={timestamp}&access_token={access_token}&sign={sign}&order_sn=210815K4QBXKJC"
        headers     = { "Content-Type": "application/json" }
        resp        = requests.get(url, headers=headers)
        ret         = json.loads(resp.content)
        
        return ret