import aiohttp
import blivedm
import http.cookies
from typing import Optional

from config import config
from .handle import InitHandler


session: Optional[aiohttp.ClientSession] = None

async def started_listening_initializer(live_config):
    await session_initializer()
    try:
        await run_single_client(live_config)
    finally:
        await session.close()
    

async def session_initializer():
    cookies = http.cookies.SimpleCookie()
    cookies["SESSDATA"] = config.b_sessdata
    cookies["SESSDATA"]["domain"] = "bilibili.com"

    global session
    session = aiohttp.ClientSession()
    session.cookie_jar.update_cookies(cookies)

async def run_single_client(live_config):
    client = blivedm.BLiveClient(live_config.rid, session=session)
    handler = InitHandler(live_config, config.debug)
    client.set_handler(handler)
    client.start()
    await client.join()
    # await client.stop_and_close()
