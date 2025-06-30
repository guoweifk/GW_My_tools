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

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en_US;q=0.9",
    "authorization": "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhaXQiOjE3NDY3OTkzMzE3MTAsImV4cCI6MTc0NjgwNjUzMTcxMCwibG9naW5fa2V5IjoiM3ljYzl3cnI1MDR3eHJhayIsInVzZXJfaWQiOiIyIiwidXNlcl9uYW1lIjoiYWRtaW4ifQ._Mo2lbx9TWGmbbTGFpOqkOHNCg3LNd4Z7-ILKd6F38yJBaeJOn-JibwtLqI3hWYVtovAkGYy6Zou62i3OpUrNA",
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

start_imsi = 466920123456005
end_imsi = 466920123456009

for imsi_num in range(start_imsi, end_imsi + 1):
    imsi_str = str(imsi_num)

    payload = {
        "algoIndex": "0",
        "amf": "8000",
        "id": "",
        "imsi": imsi_str,
        "ki": "12341234123412341234123412340000",
        "neId": "001",
        "num": 1,
        "opc": "71a121bb69baf3c0cc53fb5038a0131f"
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        print(f"IMSI: {imsi_str} | Status: {response.status_code} | Response: {response.text}")
    except requests.RequestException as e:
        print(f"IMSI: {imsi_str} | Request failed: {e}")

    time.sleep(0.1)  # 防止发送过快，可根据需要调整或去掉

print("批量注册完成！")

