import httpx
from bilibili_api import sync
from bilibili_api import user

from config import config

asyncClient = httpx.AsyncClient(
    timeout=None,
    verify=False,
    headers=config.httpx_headers
)

class bilibili_api_:
    def __init__(self):
        pass

    async def get_user_baseinfo(self, up_uid: int):
        try:
            _base_uid = user.User(up_uid, config.web_bilibili_authpack())
            _base_json = sync(_base_uid.get_user_info())
            return _base_json
        except Exception as e:
            return config._c_500

bilibili_api = bilibili_api_()
