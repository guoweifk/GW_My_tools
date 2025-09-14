from cdhd_api.http_client.https_client import https_client
from cdhd_api.config.constant_5g import get_5g_api_url, get_5g_api_body, ApiType_5g
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def cdhd_login():
    url = get_5g_api_url(ApiType_5g.USER_GET_TOKEN)
    data = get_5g_api_body(ApiType_5g.USER_GET_TOKEN)
    resp = https_client(url=url, method="POST", body=data, verify_ssl=False)
    if resp and resp.status_code == 200:
        json_data = resp.json()
        return json_data.get("data", {}).get("access_token")
    return None

def get_user_info():
    token = cdhd_login()
    if not token:
        print("Failed to get token")
        return

    url = get_5g_api_url(ApiType_5g.USER_INFO)
    data = get_5g_api_body(ApiType_5g.USER_INFO)
    resp = https_client(url=url, method="POST", body=data, auth_token=token, verify_ssl=False)
    if resp and resp.status_code == 200:
        json_data = resp.json()
        print("User Info:", json_data.get("data", {}).get("user"))
    else:
        print("Failed to get user info")

if __name__ == "__main__":
    get_user_info()
