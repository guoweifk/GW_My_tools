import json
from datetime import datetime

def print_standard_json(api_response: dict, use_api_time: bool = False):
    """
    接收接口返回的 JSON，统一格式化输出。
    - success/status/message/data 都来自 API 返回
    - data 内部的 JSON 字符串会自动递归解析
    - 默认使用当前时间，可以选择保留 API 返回的 time
    """
    def parse_nested_json(data):
        """递归解析 data 中可能存在的嵌套 JSON 字符串"""
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, str):
                    try:
                        parsed_value = json.loads(value)
                        data[key] = parse_nested_json(parsed_value)
                    except (json.JSONDecodeError, TypeError):
                        pass
                elif isinstance(value, (dict, list)):
                    data[key] = parse_nested_json(value)
        elif isinstance(data, list):
            for i, item in enumerate(data):
                if isinstance(item, str):
                    try:
                        parsed_item = json.loads(item)
                        data[i] = parse_nested_json(parsed_item)
                    except (json.JSONDecodeError, TypeError):
                        pass
                elif isinstance(item, (dict, list)):
                    data[i] = parse_nested_json(item)
        return data

    success = api_response.get("success")
    status = api_response.get("status")
    message = api_response.get("message")
    data = api_response.get("data", {})

    # 决定 time 来源
    if use_api_time and "time" in api_response:
        time_str = api_response["time"]
    else:
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    parsed_data = parse_nested_json(data)

    output_json = {
        "success": success,
        "status": status,
        "message": message,
        "time": time_str,
        "data": parsed_data
    }

    print(json.dumps(output_json, ensure_ascii=False, indent=4))

