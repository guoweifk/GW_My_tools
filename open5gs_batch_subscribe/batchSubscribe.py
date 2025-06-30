#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-03-20 10:10 
@file: batchSubscribe.py
@project: GW_My_tools
@describe: Powered By GW
"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
import time

# Open5GS API 服务器地址
API_URL = "http://192.168.55.145:9999/api/db/Subscriber"

# 认证 Token
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7Il9pZCI6IjY3NzI1YzIyN2EyZTc3MDAxNzRhMjc0YSIsInVzZXJuYW1lIjoiYWRtaW4iLCJyb2xlcyI6WyJhZG1pbiJdfSwiaWF0IjoxNzQxMDk2MDQ2fQ.dgOxhMRLW3iEySIdUi3YkDjkVyqUF4tgvVHW25-4EN0"


def register_subscriber(imsi):
    # 订阅者信息
    subscriber_data = {
        "imsi": imsi,
        "security": {
            "k": "465B5CE8B199B49FAA5F0A2EE238A6BC",
            "amf": "8000",
            "op_type": 0,
            "op_value": "E8ED289DEBA952E4283B54E88E6183CA",
            "op": None,
            "opc": "E8ED289DEBA952E4283B54E88E6183CA"
        },
        "ambr": {
            "downlink": {"value": 1, "unit": 3},
            "uplink": {"value": 1, "unit": 3}
        },
        "subscriber_status": 0,
        "operator_determined_barring": 0,
        "slice": [
            {
                "sst": 1,
                "default_indicator": True,
                "session": [
                    {
                        "name": "internet",
                        "type": 3,
                        "ambr": {
                            "downlink": {"value": 1, "unit": 3},
                            "uplink": {"value": 1, "unit": 3}
                        },
                        "qos": {
                            "index": 9,
                            "arp": {
                                "priority_level": 8,
                                "pre_emption_capability": 1,
                                "pre_emption_vulnerability": 1
                            }
                        }
                    },
                    {
                        "name": "ims",
                        "type": 3,
                        "qos": {
                            "index": 5,
                            "arp": {
                                "priority_level": 1,
                                "pre_emption_capability": 1,
                                "pre_emption_vulnerability": 1
                            }
                        },
                        "ambr": {
                            "downlink": {
                                "value": 1,
                                "unit": 3
                            },
                            "uplink": {
                                "value": 1,
                                "unit": 3
                            }
                        },
                        "ue": {},
                        "smf": {}
                    }
                ]
            }
        ]
    }

    # 请求头
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh,zh-CN;q=0.9,en;q=0.8",
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "http://192.168.55.30:9999",
        "Referer": "http://192.168.55.30:9999/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }

    # 发送请求
    # response = requests.post(API_URL, headers=headers, data=json.dumps(subscriber_data))
    response = requests.patch(API_URL, headers=headers, data=json.dumps(subscriber_data))

    # 打印结果
    print("状态码:", response.status_code)
    print("响应内容:", response.text)

def main ():
    # 批量注册 IMSI
    for i in range(1, 200):
        imsi = f"466920123456{str(i).zfill(3)}"
        print(imsi)
        time.sleep(0.5)
        register_subscriber(imsi)
if __name__ == "__main__":
    main()