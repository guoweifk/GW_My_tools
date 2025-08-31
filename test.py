#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-08-09 23:16 
@file: test.py
@project: GW_My_tools
@describe: Powered By GW
"""
start_imsi = 466920123458437
end_imsi = 466920123495000

field2 = "465b5ce8b199b49faa5f0a2ee238a6bc"
field3 = "0"
field4 = "8000"
field5 = "e8ed289deba952e4283b54e88e6183ca"

output_file = "imsi_list.txt"

with open(output_file, "w") as f:
    for imsi in range(start_imsi, end_imsi + 1):
        line = f"{imsi},{field2},{field3},{field4},{field5}\n"
        f.write(line)

print(f"生成完成，共 {end_imsi - start_imsi + 1} 行，保存在 {output_file}")
