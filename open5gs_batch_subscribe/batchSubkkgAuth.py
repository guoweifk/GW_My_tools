#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-05-09 22:34 
@file: batchSubkkgAuth.py
@project: GW_My_tools
@describe: Powered By GW
"""

import requests
import json
import time

url = "http://192.168.55.78:33030/neData/udm/auth/001"
auth = "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhaXQiOjE3NTQ4NDUxNTI1MTgsImV4cCI6MTc1NDg1MjM1MjUxOCwibG9naW5fa2V5IjoibXppY3dmbXM1dXBwZXBzYSIsInVzZXJfaWQiOiIyIiwidXNlcl9uYW1lIjoiYWRtaW4ifQ.D7MKqlEnqJqNjfcTedxWZUsYWOxKj5lq77AgC2pLMCmN1ShSg95_38oFuNyx3spwO2rpslTiG38DUo-Csrxwlw"
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en_US;q=0.9",
    "authorization": auth,
    "cache-control": "max-age=0",
    "connection": "keep-alive",
    "content-type": "application/json;charset=utf-8",
    "host": "192.168.55.78:33030",
    "origin": "http://192.168.55.78",
    "referer": "http://192.168.55.78/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "x-app-code": "OMC",
    "x-app-version": "2.240927"
}

start_imsi = 466920123497001
end_imsi = 466920123507001

for imsi_num in range(start_imsi, end_imsi + 1):
    imsi_str = str(imsi_num)

    payload = {
        "algoIndex": "0",
        "amf": "8000",
        "id": "",
        "imsi": imsi_str,
        "ki": "465B5CE8B199B49FAA5F0A2EE238A6BC",
        "neId": "001",
        "num": 5,
        "opc": "E8ED289DEBA952E4283B54E88E6183CA"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        print(f"IMSI: {imsi_str} | Status: {response.status_code} | Response: {response.text}")
    except requests.RequestException as e:
        print(f"IMSI: {imsi_str} | Request failed: {e}")

    time.sleep(0.01)  # 防止发送过快，可根据需要调整或去掉

print("批量注册完成！")
