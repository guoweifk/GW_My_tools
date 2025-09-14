#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-08-04 13:02 
@file: constant.py
@project: GW_My_tools
@describe: Powered By GW
"""

# === 5G配置 ===
# === 基础配置 ===
FIVEG_SERVER_IP = "192.168.1.201"
FIVEG_URL = f"https://{FIVEG_SERVER_IP}"

# ===== 用户接口 =====
API_USER_TOKEN = "/api/user/token"                        # 获取访问令牌 ✅
API_USER_INFO = "/api/user/info"                          # 用户信息 ✅
API_USER_REGISTER = "/api/user/register"                  # 用户注册 ✅
API_USER_UPDATE_PASSWORD = "/api/user/updatePassword"     # 修改密码 ✅
API_USER_GET_TICKET = "/api/user/getTicket"               # 获取 ticket（web 登录）✅
API_WEB_LOGIN = "/webtokenLogin/login?ticket={ticket}"    # 自动登录 ✅

# ===== 测试任务相关 =====
API_ORDER_UNIFIED = "/api/order/unifiedorder"             # 下发测试任务
API_ORDER_RUN = "/api/order/pushList"                     # 运行测试用例 ✅
API_ORDER_QUERY = "/api/order/orderquery"                 # 查询订单信息 ✅
API_ORDER_STOP = "/api/order/stop"                        # 停止测试任务 ✅

# ===== 文件处理 =====
API_FILE_UPLOAD = "/api/upload/fileUpload"                # 文件上传
API_FILE_DOWNLOAD = "/api/fileDownload"                   # 文件下载
API_PCAP_DOWNLOAD = "/api/pcapDownload"                   # 抓包文件下载
API_STATS_DOWNLOAD = "/api/statsDataDownload"             # 网元统计数据下载

# ===== 实时 & 系统数据 =====
API_REALTIME_MONITOR = "/api/data/monitor"                # 实时监控数据 ✅
API_GET_NIC = "/api/getnic"                               # 获取网卡信息 ✅
API_NS_STATUS = "/api/ns_service/status"                  # 主程序状态 ✅
API_MESSAGE_SEND = "/api/message/send"                    # 消息实时推送
# ===== 用户信息 =====
EMAIL = "dotouch@dotouch.com.cn"
PASSWD = "dotouch"

# ===== 文件路径 =====
FILE_PATH = "/cdhd_api/file"


