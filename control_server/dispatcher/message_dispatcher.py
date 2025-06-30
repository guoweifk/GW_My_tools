#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-06-29 20:50 
@file: message_dispatcher.py
@project: GW_My_tools
@describe: Powered By GW
"""
# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-06-28 22:56 
@file: message_dispatcher.py
@project: GW_My_tools
@describe: Powered By GW
"""
from control_server.dispatcher.agent_netem_command_processor import AgentNetemCommandProcessor
from control_server.dispatcher.agent_traffic_command_processor import AgentTrafficCommandProcessor
from control_server.dispatcher.server_traffic_command_processor import ServerTrafficCommandProcessor
from control_server.message.base_message import AgentNetemControlMessage, AgentTrafficMessage
from control_server.utils.logutil import get_logger

logger = get_logger("message_dispatcher")


class ServerMessageDispatcher:
    def __init__(self):
        self.netem_processor = AgentNetemCommandProcessor()
        self.agent_traffic_processor = AgentTrafficCommandProcessor()
        self.server_traffic_processor = ServerTrafficCommandProcessor()

    def dispatch(self, msg):
        msg_type = msg.get("type")
        logger.info(f"msg:" + msg_type)

        if msg_type == "agent_netem":
            msg_obj = AgentNetemControlMessage.from_dict(msg)
            self.netem_processor.handle(msg_obj)

        elif msg_type == "agent_traffic":
            self.agent_traffic_processor.handle(msg)

        elif msg_type == "server_traffic":
            self.server_traffic_processor.handle(msg)

        else:
            logger.warning(f"[!] 未知消息类型: {msg_type}")
