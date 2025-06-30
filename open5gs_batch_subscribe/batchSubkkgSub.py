#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-05-09 22:38 
@file: batchSubkkgSub.py
@project: GW_My_tools
@describe: Powered By GW
"""
import requests
import json
import time

url = "http://192.168.55.78:33030/neData/udm/sub/001"

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

start_imsi = 466920123456003
end_imsi = 466920123456009
start_msisdn = 13392701017  # 基础手机号起点

for idx, imsi_num in enumerate(range(start_imsi, end_imsi + 1), start=4):
    imsi_str = str(imsi_num)
    msisdn_str = str(start_msisdn + (imsi_num - start_imsi))

    payload = {
        "ambr": "def_ambr",
        "apnContext": "010200000000",
        "ard": "65",
        "arfb": "def_arfb",
        "cag": "",
        "cn": "3",
        "contextId": "1",
        "epsDat": "1,64,24,65,def_eps,1,2,010200000000,-",
        "epsFlag": "1",
        "epsOdb": "64",
        "epstpl": "def_eps",
        "hplmnOdb": "24",
        "id": str(idx),
        "imsi": imsi_str,
        "msisdn": msisdn_str,
        "neId": "001",
        "nssai": "def_nssai",
        "num": 1,
        "rat": "0",
        "remark": "",
        "rfsp": 1,
        "sar": "def_sar",
        "smData": "1-000001&internet&ims",
        "smfSel": "def_snssai",
        "staticIp": "-",
        "ueType": 1
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        print(f"IMSI: {imsi_str} | MSISDN: {msisdn_str} | Status: {response.status_code} | Response: {response.text}")
    except requests.RequestException as e:
        print(f"IMSI: {imsi_str} | Request failed: {e}")

    time.sleep(0.1)  # 调整请求频率，防止压力过大

print("批量订阅完成！")
