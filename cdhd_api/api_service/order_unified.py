#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-09-14
@file: clone_order_ran.py
@project: GW_My_tools
@describe: 根据本地订单 JSON 文件新建一个订单
"""
'''
它会自动生成一个新工程5gApi，在里面执行新的订单，而且执行失败，sss
'''

import os
import copy
import json
from cdhd_api.http_client.https_client import https_client
from cdhd_api.config.constant_5g import get_5g_api_url, ApiType_5g
import urllib3
from cdhd_api.api_service.login import cdhd_login
from cdhd_api.config.json_parser import print_standard_json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def build_new_order_payload(order_data: dict) -> dict:
    """
    根据订单查询结果，构造新建订单的请求体
    """
    order_detail = copy.deepcopy(order_data.get("order_detail", {}))

    # 构造新订单 payload（去掉系统生成的字段）
    new_order = {
        "project_id": order_data.get("project_id"),
        "project_name": order_data.get("project_name"),
        "cur_app": order_data.get("cur_app", "sim_5gc"),
        "order_detail": order_detail,
        "desc": order_data.get("desc", "Cloned order"),
        "channel": order_data.get("channel", 1),
        "user_id": order_data.get("user_id", 1),
        "version": order_data.get("order_detail", {}).get("version", "2.5.0"),
    }

    return new_order


if __name__ == "__main__":
    # 本地 JSON 文件路径（你生成的 JSON 文件）
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    JSON_FILE = os.path.join(BASE_DIR, "..", "file","query_resp.json")  # 改成你自己的 JSON 文件名

    # 读取本地 JSON 文件
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            local_json = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {JSON_FILE}")
        exit(1)
    except ValueError as e:
        print("JSON decode failed:", e)
        exit(1)

    # 构造新订单 payload
    order_data = local_json.get("data", {})
    new_order_payload = build_new_order_payload(order_data)

    # 调用创建订单接口
    url = get_5g_api_url(ApiType_5g.ORDER_UNIFIED)
    access_token = cdhd_login()

    resp = https_client(
        url=url,
        method="POST",
        body=new_order_payload,
        auth_token=access_token,
        verify_ssl=False
    )

    if resp and resp.status_code == 200:
        try:
            json_data = resp.json()
            print_standard_json(json_data, use_api_time=True)
        except ValueError as e:
            print("JSON decode failed:", e)
    else:
        print("Failed to create order, status:", resp.status_code if resp else "No response")
