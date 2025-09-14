#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-08-04 12:53 
@file: https_client.py
@project: GW_My_tools
@describe: Powered By GW
"""
import requests
def https_client(
    url: str,
    method: str = "POST",
    body: dict = None,
    params: dict = None,
    headers: dict = None,
    auth_token: str = None,
    timeout: int = 10,
    verify_ssl: bool = False

):
    """
    通用 HTTPS 客户端函数，用于发送自定义的 HTTP 请求

    :param url: 请求完整 URL（如 https://example.com/api）
    :param method: 请求方法（如 "GET", "POST", "PUT", "DELETE"）
    :param body: 请求体 JSON（仅适用于 POST/PUT）
    :param params: URL 查询参数（仅适用于 GET）  # ✅ 新增
    :param headers: 自定义请求头（可选）
    :param auth_token: Bearer token（可选，会自动加到 Authorization 头中）
    :param timeout: 请求超时时间（单位：秒）
    :param verify_ssl: 是否校验证书（默认为 False）
    :return: requests.Response 对象 或 None
    """
    session = requests.Session()

    # 构造默认 headers
    default_headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=utf-8",
        "User-Agent": "CustomHTTPSClient/1.0"
    }

    # 如果传入了 auth_token，就添加 Authorization 头
    if auth_token:
        default_headers["Authorization"] = f"Bearer {auth_token}"

    # 合并 headers
    if headers:
        default_headers.update(headers)

    try:
        # 根据方法选择发送方式
        if method.upper() == "GET":
            response = session.get(url, headers=default_headers, params=params, timeout=timeout, verify=verify_ssl)
        elif method.upper() == "POST":
            response = session.post(url, headers=default_headers, json=body, timeout=timeout, verify=verify_ssl)
        elif method.upper() == "PUT":
            response = session.put(url, headers=default_headers, json=body, timeout=timeout, verify=verify_ssl)
        elif method.upper() == "DELETE":
            response = session.delete(url, headers=default_headers, timeout=timeout, verify=verify_ssl)
        else:
            raise ValueError(f"Unsupported method: {method}")

        print(f"[HTTPS Client] Status: {response.status_code} | URL: {url}")
        return response

    except requests.RequestException as e:
        print(f"[HTTPS Client] Request failed: {e}")
        return None
