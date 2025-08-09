#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-08-04 17:35 
@file: order_ran.py
@project: GW_My_tools
@describe: Powered By GW
"""
# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-08-04 12:57
@file: login.py
@project: GW_My_tools
@describe: Powered By GW
"""
from cdhd_api.http_client.https_client import https_client
from cdhd_api.config.constant_5g import get_5g_api_url, ApiType_5g
import urllib3
from cdhd_api.api_service.login import cdhd_login

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == "__main__":
    url = get_5g_api_url(ApiType_5g.ORDER_RUN)
    data = {"order_no": "20250723172931_51"}
    access_token = cdhd_login()
    token_resp = https_client(
        url=url,
        method="POST",
        body=data,
        auth_token=access_token,
        verify_ssl=False
    )
    if token_resp and token_resp.status_code == 200:
        try:
            json_data = token_resp.json()
            message = json_data.get('message')
            print("message:", message)
        except ValueError as e:
            print("JSON decode failed:", e)
    else:
        print("Failed to get response or status code != 200")
