from cdhd_api.http_client.https_client import https_client
from cdhd_api.config.constant_5g import get_5g_api_url, ApiType_5g
from cdhd_api.api_service.login import cdhd_login
from cdhd_api.config.constant_config import FIVEG_SERVER_IP
from cdhd_api.config.json_parser import print_standard_json
import urllib3
import webbrowser
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def login_with_ticket(email: str, password: str):
    """
    1. 使用邮箱和密码获取 ticket
    2. 用 ticket 自动登录
    3. 打印两个接口返回的 JSON
    """
    # 1️⃣ 获取 ticket
    url_ticket = get_5g_api_url(ApiType_5g.USER_GET_TICKET)
    access_token = cdhd_login()
    data = {"email": email, "password": password}

    resp_ticket = https_client(
        url=url_ticket,
        method="POST",
        body=data,
        auth_token=access_token,
        verify_ssl=False
    )

    if not resp_ticket or resp_ticket.status_code != 200:
        print("Failed to get ticket or status code != 200")
        return

    try:
        ticket_json = resp_ticket.json()
        print("=== 获取 ticket 返回 ===")
        print_standard_json(ticket_json)
        ticket = ticket_json.get("data", {}).get("ticket")
        if not ticket:
            print("No ticket returned from API")
            return
    except ValueError as e:
        print("JSON decode failed for ticket:", e)
        return

    url_login = f"https://{FIVEG_SERVER_IP}/webtokenLogin/login?ticket={ticket}"
    resp_login = https_client(
        url=url_login,
        method="GET",
        auth_token=None,  # 自动登录用 ticket，不用 Bearer token
        verify_ssl=False
    )

    # 打开浏览器访问 URL
    webbrowser.open(url_login)

    if not resp_login:
        print("Auto login request failed")
        return

    # 3️⃣ 打印自动登录返回
    if resp_login.status_code == 200:
        try:
            login_json = resp_login.json()
            print("=== 自动登录返回 ===")
            print_standard_json(login_json)
        except ValueError:
            print(f"Auto login succeeded, server returned status: {resp_login.status_code} No Content")
    elif resp_login.status_code == 204:
        # 204 表示 No Content，但登录成功，不打印失败信息
        print(f"Auto login succeeded, server returned status: {resp_login.status_code} No Content")
    else:
        print(f"Auto login failed, status: {resp_login.status_code}")

if __name__ == "__main__":
    login_with_ticket(email="dotouch@dotouch.com.cn", password="dotouch")
