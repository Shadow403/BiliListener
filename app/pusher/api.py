import httpx
from config import BiliConfig

HTTPClient = httpx.AsyncClient(
        timeout=None,
        verify=False
    )

async def QueryLive(uid_list):
    ret = (await HTTPClient.post(BiliConfig.LIVE_NOTICE, headers=BiliConfig.HEADERS, json=uid_list)).json()
    return ret
