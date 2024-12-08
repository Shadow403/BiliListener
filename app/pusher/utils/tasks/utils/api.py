import httpx
from config import BiliConfig

HTTPClient = httpx.Client(
        verify=False,
        timeout=None,
        headers=BiliConfig.HEADERS
    )

def api_query_live_status(uid_list):
    ret = HTTPClient.post(BiliConfig.LIVE_NOTICE, json=uid_list).json()
    return ret
