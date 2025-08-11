#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: GW
@time: 2025-08-09 22:09 
@file: batchCreateKKGauthImportText.py
@project: GW_My_tools
@describe: Powered By GW
"""

import csv

# -------- 可按需修改的参数 --------
start_imsi = 466920123458437
end_imsi   = 466920123458438


# 固定字段（来自你之前的样例）
ki_fixed   = "888440695bce54644423da49053d6e74b95374ba8ddff8c2"
status_val = 1
amf_val    = 8000
opc_fixed  = "bbfd0ccb02e7203708723c37f3d0ee8ab95374ba8ddff8c2"

# 你表里需要的其他列
ne_id_val     = ""   # 如果没有要求，可保持默认或改成你需要的
algo_index_val = 0       # 没要求就填 0
# --------------------------------

output_file = "imsi_batch.csv"

with open(output_file, "w", newline="") as f:
    w = csv.writer(f)
    # 写表头
    w.writerow(["id", "imsi", "ne_id", "amf", "status", "ki", "algo_index", "opc"])

    for imsi in range(start_imsi, end_imsi + 1):
        # id 使用 \N 代表 NULL，方便 MySQL 自增（LOAD DATA 时会识别为 NULL）
        w.writerow(["", str(imsi), ne_id_val, amf_val, status_val, ki_fixed, algo_index_val, opc_fixed])

print(f"已生成 {output_file}，共 {end_imsi - start_imsi + 1} 条记录。")

