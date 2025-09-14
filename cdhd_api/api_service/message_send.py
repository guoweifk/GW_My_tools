from cdhd_api.http_client.https_client import https_client
from cdhd_api.config.constant_5g import get_5g_api_url, ApiType_5g
from cdhd_api.api_service.login import cdhd_login
import urllib3
from cdhd_api.config.json_parser import print_standard_json  # 导入函数

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == "__main__":
    url = get_5g_api_url(ApiType_5g.MESSAGE_SEND)
    access_token = cdhd_login()
    token_resp = https_client(
        url=url,
        method="POST",
        auth_token=access_token,
        verify_ssl=False
    )

    if token_resp and token_resp.status_code == 200:
        try:
            json_data = token_resp.json()
            print_standard_json(json_data)
        except ValueError as e:
            print("JSON decode failed:", e)
    else:
        print("Failed to get response or status code != 200")
