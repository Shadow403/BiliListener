import httpx

asyncClient = httpx.AsyncClient(
    timeout=None,
    verify=False,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70"
    }
)

class bilibili_api:
    def __init__(self):
        self.root = "https://api-dev.shadow403.com.cn/api/bilibili"

    async def get_user_baseinfo(self, uid):
        ret_dict = (await asyncClient.get(f"{self.root}/v1/user/base_info/")).json()
        return ret_dict

