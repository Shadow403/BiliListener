import os
from bilibili_api import Credential, sync
from fastapi.openapi.models import Contact

from . import __version__
from .utils import read_config


class BaseConfig:
    def __init__(self, config_data):
        __PATH__: str = os.getcwd()

        self.host: str = config_data["api"]["host"]
        self.port: int = config_data["api"]["port"]

        self.ws_port: int = config_data["api"]["ws_port"]
        self.ws_hub: int = config_data["api"]["ws_push_delay"]["hub"]
        self.ws_listening: int = config_data["api"]["ws_push_delay"]["listening"]
    
        self.cors: list = config_data["api"]["cors"]
        self.pravite_router: dict = config_data["api"]["router_access"]
        self.strict: bool = self.pravite_router["strict"]
        self.acc_put_uid: list = self.pravite_router["r_put_uid"]

        self.appver: str = __version__ + " "
        self.ws_perfix: str = ""
        self.http_perfix: str = "/api"

        self.tags: list = ["API 💾"]
        self.appname: str = "BiliListener"

        self._c_404: dict = {"code": 404, "message": "notfound", "data": {}}
        self._c_422: dict = {"code": 422, "message": "parm error | method not allowed", "data": {}}
        self._c_500: dict = {"code": 500, "message": "internal server error", "data": {}}

        self.ct_info: Contact = Contact(
            name=self.appname,
            email="admin@shadow403.cn",
            url="https://live.shadow403.cn"
        )

        self.lc_info: dict = {
            "name": "Apache License Version 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        }

        self.sw_ico: str = "https://swagger-cdn.pages.dev/static/favicon.png"
        self.sw_css: str = "https://swagger-cdn.pages.dev/static/swagger-ui_v2.css"
        self.sw_jvs: str = "https://swagger-cdn.pages.dev/static/swagger-ui-bundle_v2.js"
        self.web_desc: str = "Application Programming Interface 📡"
        self.web_oapi: str = "/openapi"

        self._et: int = 1000
        self._dm: int = 1001
        self._gf: int = 1002
        self._g_gf: int = 10020
        self._s_gf: int = 10021
        self._gd: int = 1003
        self._sc: int = 1004

        self.httpx_headers: dict = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 Edg/103.0.1264.41"
        }
        self.auth: str = config_data["auth"]
        self.b_bili_jct: str = self.auth["bili_jct"]
        self.b_sessdata: str = self.auth["sessdata"]
        self.live_push_url: str = "https://api.live.bilibili.com/room/v1/Room/get_status_info_by_uids"
        self.push_query_delay: int = config_data["live_query_delay"]
        self.live_clear_delay: int = config_data["live_clear_delay"]

        self.root: str = f"{__PATH__}/{config_data['data']['root']}"
        self.db_path: str = f"{self.root}/{config_data['data']['db_path']}"

        self.json_enable: bool = config_data["data"]["json"]["enable"]
        self.json_path: str = f"{self.root}/{config_data['data']['json']['json_path']}"
        self.debug: bool = config_data["debug"]

        if self.debug:
            self.hide_console: bool = False
        else:
            self.hide_console: bool = config_data["hide_console"]

    def web_bilibili_authpack(self):
        authpack = Credential(
            sessdata=self.b_sessdata, 
            buvid3=None,
            bili_jct=self.b_bili_jct, 
            dedeuserid=None,
            ac_time_value=None
        )
        token_refresh = sync(authpack.check_refresh())

        if token_refresh:
            authpack = sync(authpack.refresh())

        return authpack

config: BaseConfig = BaseConfig(read_config())


class Router:
    v1_root: str = f"{config.http_perfix}/v1"
    v2_root: str = f"{config.http_perfix}/v2"
    web_root: str = f"{config.http_perfix}/web"

    ws_v1_root: str = f"{config.ws_perfix}/v1"

    ws_tags: list = ["WS 📡"]
    ws_perfix: str = "/ws"

    web_tags: list = ["WEB 🌐"]
    web_perfix: str = ""

    stats_tags: list = ["STATS 📈"]
    stats_perfix: str = "/stats"

    info_tags: list = ["INFO 📜"]
    info_perfix: str = "/info"

    edit_tags: list = ["EDIT 🔧"]
    edit_perfix: str = "/edit"

    livelogs_tags: list = ["LIVELOGS 📚"]
    livelogs_perfix: str = "/live"

