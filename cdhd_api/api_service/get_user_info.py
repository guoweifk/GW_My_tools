#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-08-04 13:20 
@file: get_user_info.py
@project: GW_My_tools
@describe: Powered By GW
"""
from cdhd_api.http_client.https_client import https_client
from cdhd_api.config.constant_5g import get_5g_api_url, get_5g_api_body, ApiType_5g
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == "__main__":
    url = get_5g_api_url(ApiType_5g.USER_INFO)
    data = get_5g_api_body(ApiType_5g.USER_INFO)

    token_resp = https_client(
        url=url,
        auth_token="eyJpdiI6IkdvQTMyZVU0eUZEZ1oycjJlT1NnXC9BPT0iLCJ2YWx1ZSI6InZMS3J2V0VwaEJGNENpTjI3MmltOWp0dUxpWUhjOVNOWjFCSFwvaGVLY09vPSIsIm1hYyI6IjAyZGIzZTFlOGU2NzI5OTFhMTJjNWFlMTc2MWRhNmU0ZjQwNzBlYmFkMDg1NWM5ZDdkNTAxMDA2OGY4ZjAwNDIifQ==",
        method="POST",
        body=data,
        verify_ssl=False
    )
    if token_resp and token_resp.status_code == 200:
        try:
            json_data = token_resp.json()
            user = json_data.get('data', {}).get('user')
            print("Access Token:", user)
        except ValueError as e:
            print("JSON decode failed:", e)
    else:
        print("Failed to get response or status code != 200")
