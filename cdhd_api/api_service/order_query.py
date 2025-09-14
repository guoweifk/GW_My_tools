#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-08-04 17:35 
@file: order_ran.py
@project: GW_My_tools
@describe: Powered By GW
"""

from cdhd_api.http_client.https_client import https_client
from cdhd_api.config.constant_5g import get_5g_api_url, ApiType_5g
import urllib3
from cdhd_api.api_service.login import cdhd_login
from cdhd_api.config.json_parser import print_standard_json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == "__main__":
    url = get_5g_api_url(ApiType_5g.ORDER_QUERY)
    data = {"order_no": "20250905082518_3816"}
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
            # 单独获取 data
            data_field = json_data.get('data', {})
            if data_field and data_field.get("order_no"):
                print_standard_json(json_data, use_api_time=True)
            else:
                print("No order data returned")

        except ValueError as e:
            print("JSON decode failed:", e)
    else:
        print("Failed to get response or status code != 200")
