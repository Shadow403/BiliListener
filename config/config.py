import os
import dotenv

class WebAPI:
    HOST: str = "127.0.0.1"
    PORT: int = 8080
    PREFIX: str = "/api"
    _c_404: dict = {"code": 404, "message": "notfound", "data": {}}
    _c_500: dict = {"code": 500, "message": "internal server error", "data": {}}

class BiliConfig:
    _et: int = 1000
    _dm: int = 1001
    _gf: int = 1002
    _gd: int = 1003
    _sc: int = 1004

    HEADERS: dict = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 Edg/103.0.1264.41"
    }
    QUERYDELAY: int = 30
    SESSDATA: str = "<这里填已登录B站的 SESSDATA>"
    LIVE_NOTICE: str = "https://api.live.bilibili.com/room/v1/Room/get_status_info_by_uids"

class PathConfig:
    __PATH__: str = os.getcwd()
    DATA_Path: str = f"{__PATH__}/data"
    CACHE_Path: str = f"{__PATH__}/config/data/cache.json"
    UIDLIST_Path: str = f"{__PATH__}/config/data/uid_list.json"
