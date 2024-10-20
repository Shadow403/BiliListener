import httpx
from config import BiliConfig

def QueryLive(uid_list):
    ret = httpx.post(BiliConfig.LIVE_NOTICE, headers=BiliConfig.HEADERS, json=uid_list).json()
    return ret
