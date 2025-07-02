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
from control_server.message.base_message import ServerPythonCommandMessage, ServerPythonCommandPayload
from concurrent.futures import ThreadPoolExecutor, as_completed

logger = get_logger("load_control_manager")

logger.info("日志初始化成功")
logger.setLevel(logging.INFO)


class ServerPythonCommandProcessor(BaseProcessor):
    def __init__(self, max_workers=5):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def handle(self, msg: ServerPythonCommandMessage):
        if not msg.payload:
            logger.warning("[×] 收到空 payload，跳过执行")
            return

        futures = []
        for payload in msg.payload:
            command = payload.command
            timeout = payload.time_out
            futures.append(
                self.executor.submit(self._run_command, command, timeout)
            )

        # 可选：等待所有命令完成（也可以不等）
        for future in as_completed(futures):
            _ = future.result()

    def _run_command(self, command: str, timeout: float):
        logger.info(f"[✓] 开始执行命令: {command}")
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            logger.info(f"[→] 命令执行完成: {command}\n输出:\n{result.stdout}")
            if result.stderr:
                logger.warning(f"[!] 错误输出:\n{result.stderr}")
        except subprocess.TimeoutExpired:
            logger.error(f"[×] 命令超时: {command}")
        except Exception as e:
            logger.error(f"[×] 执行异常: {command} -> {e}")
