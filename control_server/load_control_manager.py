#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: LX
@time: 2025-06-23 18:24 
@file: load_control_manager.py
@project: GW_My_tools
@describe: Powered By LX
"""

import socket
import json
import os
import sys

from control_server.utils.logutil import get_logger

logger = get_logger("load_control_manager")
SERVER_PORT = 22222  # 容器内部 agent 监听端口

# 把项目根目录加入 sys.path，比如 /tmp/pycharm_project_458
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)
logger.info(f"PROJECT_ROOT {PROJECT_ROOT}")

from control_server.dispatcher.message_dispatcher import ServerMessageDispatcher


def start_server():
    dispatcher = ServerMessageDispatcher()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('0.0.0.0', SERVER_PORT))
        server_socket.listen(5)
        logger.info(f"[启动] Server 监听端口 {SERVER_PORT}")

        while True:
            try:
                client_socket, client_address = server_socket.accept()
                with client_socket:
                    raw_data = client_socket.recv(65535)
                    logger.info(f"[数据] 接收到来自 {client_address[0]} 的原始数据")

                    if raw_data:
                        message = json.loads(raw_data.decode())
                        dispatcher.dispatch(message)
                    else:
                        logger.warning("[!] 空消息")
            except Exception as e:
                logger.error(f"[×] 处理异常: {e}")


if __name__ == "__main__":
    start_server()
