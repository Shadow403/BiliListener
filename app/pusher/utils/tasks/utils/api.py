import httpx
from config import config

HTTPClient = httpx.Client(
        verify=False,
        timeout=None,
        headers=config.httpx_headers
    )

def api_query_live_status(uid_list):
    ret = HTTPClient.post(config.live_push_url, json=uid_list).json()
    return ret
