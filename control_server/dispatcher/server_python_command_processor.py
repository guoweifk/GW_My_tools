#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-07-01 18:33 
@file: server_python_command_processor.py
@project: GW_My_tools
@describe: Powered By GW
"""
from control_server.dispatcher.base_processor import BaseProcessor
import logging
import subprocess
from control_server.utils.logutil import get_logger
from control_server.message.base_message import ServerPythonCommandMessage,ServerPythonCommandPayload

logger = get_logger("load_control_manager")

logger.info("日志初始化成功")
logger.setLevel(logging.INFO)


class ServerPythonCommandProcessor(BaseProcessor):
    def __init__(self):
        pass

    def handle(self, msg: ServerPythonCommandMessage):
        if not msg.payload:
            logger.warning("[×] 收到空 payload，跳过执行")
            return

        for payload in msg.payload:
            command = payload.command
            logger.info(f"[✓] 执行 Shell 命令: {command}")

            try:
                result = subprocess.run(
                    command,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout= 5
                )
                logger.info(f"[→] 命令执行成功，输出如下:\n{result.stdout}")
                if result.stderr:
                    logger.warning(f"[!] 命令错误输出:\n{result.stderr}")
            except subprocess.TimeoutExpired:
                logger.error(f"[×] 命令执行超时: {command}")
            except Exception as e:
                logger.error(f"[×] 命令执行异常: {e}")
