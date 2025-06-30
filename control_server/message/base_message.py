#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-06-29 16:52 
@file: base_message.py
@project: GW_My_tools
@describe: Powered By GW
"""

from control_server.message.toAgentPayloads.netem import ServerToAgentNetemPayload,AgentNetemPayload
from control_server.message.toAgentPayloads.traffic import ServerToAgentTrafficPayload,AgentTrafficPayload
from control_server.message.serverPayloads.server_traffic import ServerTrafficPayload
from dataclasses import dataclass
from typing import Optional,List
from abc import ABC


# server收到的消息
@dataclass
class BaseServerControlMessage(ABC):
    type: str
    timestamp: Optional[str]
    target_server_ip: str


# center发来的控制agent的消息
@dataclass
class AgentNetemControlMessage(BaseServerControlMessage):
    payload: ServerToAgentNetemPayload

    @staticmethod
    def from_dict(d: dict) -> "AgentNetemControlMessage":
        return AgentNetemControlMessage(
            type=d["type"],
            timestamp=d.get("timestamp"),
            target_server_ip=d["target_server_ip"],
            payload=ServerToAgentNetemPayload.from_dict(d["payload"])
        )


# center发来的控制agent的消息
@dataclass
class AgentTrafficControlMessage(BaseServerControlMessage):
    payload: ServerToAgentTrafficPayload

    @staticmethod
    def from_dict(d: dict) -> "AgentTrafficControlMessage":
        return AgentTrafficControlMessage(
            type=d["type"],
            timestamp=d.get("timestamp"),
            target_server_ip=d["target_server_ip"],
            payload=ServerToAgentTrafficPayload.from_dict(d["payload"])
        )


# center发来的控制server的消息
@dataclass
class ServerTrafficControlMessage(BaseServerControlMessage):
    payload: List[ServerTrafficPayload]

    @staticmethod
    def from_dict(d: dict) -> "ServerTrafficControlMessage":
        return ServerTrafficControlMessage(
            type=d["type"],
            timestamp=d.get("timestamp"),
            target_server_ip=d["target_server_ip"],
            payload=[ServerTrafficPayload.from_dict(p) for p in d["payload"]]
        )


# 发给agent的消息
@dataclass
class BaseAgentControlMessage(ABC):
    type: str
    timestamp: Optional[str]


@dataclass
class AgentNetemMessage(BaseAgentControlMessage):
    payload: AgentNetemPayload


@dataclass
class AgentTrafficMessage(BaseAgentControlMessage):
    payload: List[AgentTrafficPayload]
