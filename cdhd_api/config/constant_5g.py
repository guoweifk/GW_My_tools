#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-08-04 13:07 
@file: 5g_constant.py
@project: GW_My_tools
@describe: Powered By GW
"""
from cdhd_api.config.constant_config import *

from enum import Enum


class ApiType_5g(Enum):
    USER_GET_TOKEN = "USER_GET_TOKEN"
    USER_INFO = "USER_INFO"
    ORDER_UNIFIED = "ORDER_UNIFIED"
    ORDER_RUN = "ORDER_RUN"
    FILE_UPLOAD = "FILE_UPLOAD"
    GET_NIC = "GET_NIC"
    NS_STATUS = "NS_STATUS"
    USER_GET_TICKET = "USER_GET_TICKET"
    USER_REGISTER = "USER_REGISTER"
    USER_UPDATE_PASSWORD = "USER_UPDATE_PASSWORD"
    WEB_LOGIN = "WEB_LOGIN"

    # 可继续添加其他接口类型


# ========== 工具函数 ==========
def get_5g_api_url(api_type: ApiType_5g, **kwargs) -> str:
    path_map = {
        ApiType_5g.USER_GET_TOKEN: API_USER_TOKEN,
        ApiType_5g.USER_INFO: API_USER_INFO,
        ApiType_5g.ORDER_UNIFIED: API_ORDER_UNIFIED,
        ApiType_5g.ORDER_RUN: API_ORDER_RUN,
        ApiType_5g.FILE_UPLOAD: API_FILE_UPLOAD,
        ApiType_5g.GET_NIC: API_GET_NIC,
        ApiType_5g.NS_STATUS: API_NS_STATUS,
        ApiType_5g.USER_GET_TICKET: API_USER_GET_TICKET,
        ApiType_5g.USER_REGISTER: API_USER_REGISTER,
        ApiType_5g.USER_UPDATE_PASSWORD: API_USER_UPDATE_PASSWORD,
        ApiType_5g.WEB_LOGIN: API_WEB_LOGIN.format(ticket=kwargs.get("ticket", ""))
    }
    if api_type not in path_map:
        raise ValueError(f"Unsupported API type: {api_type}")

    return FIVEG_URL + path_map[api_type]


def get_5g_api_body(api_type: ApiType_5g) -> dict:
    if api_type == ApiType_5g.USER_GET_TOKEN:
        # === 固定登录请求体 ===
        API_USER_TOKEN_PAYLOAD = {
            "email": EMAIL,
            "password": PASSWD
        }
        return API_USER_TOKEN_PAYLOAD
    elif api_type == ApiType_5g.USER_INFO:
        API_USER_INFO_PAYLOAD = {
            "email": EMAIL,
        }
        return API_USER_INFO_PAYLOAD
    else :
        return {}  # 默认返回空 body，可按需添加
