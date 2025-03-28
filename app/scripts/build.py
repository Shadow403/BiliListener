import os

from config import __version__, __platform__, get_type

__ico_path__ = "./scripts/ico/"

ex = get_type()

def build_main():
    _build_ico = f"-i {__ico_path__}listener.ico"
    _bulid_name_ = f"-n pusher-{__platform__}-{__version__}-{ex}"

    _hi_curl_cffi = "--hidden-import curl_cffi --hidden-import bilibili_api.clients.CurlCFFIClient"
    _hi_aiohttp = "--hidden-import aiohttp --hidden-import bilibili_api.clients.AioHTTPClient"
    _hi_httpx = "--hidden-import httpx --hidden-import bilibili_api.clients.HTTPXClient"
    
    os.system(f"pyinstaller {_build_ico} --onefile pusher.py {_bulid_name_} {_hi_curl_cffi} {_hi_aiohttp} {_hi_httpx} --clean")
