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
API_URL = "http://192.168.55.186:9999/api/db/Subscriber"

# 认证 Token
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7Il9pZCI6IjY4NWU0ODQ1MmFkN2UyMDAxN2M4ZGRlZiIsInVzZXJuYW1lIjoiYWRtaW4iLCJyb2xlcyI6WyJhZG1pbiJdfSwiaWF0IjoxNzU0OTI2MzcxfQ.fm3h6hfOrogAex__42AaPY1Vo-lFHU5bZLkOroUEIfI"


def register_subscriber(imsi):
    # 订阅者信息
    subscriber_data = {
        "imsi": imsi,
        "security": {
            "k": "8BAF473F2F8FD09487CCCBD7097C6862",
            "amf": "8000",
            "op_type": 0,
            "op_value": "E8ED289DEBA952E4283B54E88E618ABC",
            "op": None,
            "opc": "E8ED289DEBA952E4283B54E88E618ABC"
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
                # "sd": "000001",
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
    response = requests.post(API_URL, headers=headers, data=json.dumps(subscriber_data))

    # 打印结果
    print("状态码:", response.status_code)
    print("响应内容:", response.text)

def main ():
    # 批量注册 IMSI
    start_imsi = 466920000001006
    end_imsi = 466920000011006
    # end_imsi = 466920000021002

    for imsi_num in range(start_imsi, end_imsi + 1):
        imsi = str(imsi_num)
        print(imsi)
        time.sleep(0.02)
        register_subscriber(imsi)
if __name__ == "__main__":
    main()