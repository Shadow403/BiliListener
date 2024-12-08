import aiohttp
import blivedm
import http.cookies
from typing import Optional

from .handle import InitHandler
from config.config import BiliConfig


session: Optional[aiohttp.ClientSession] = None

async def started_listening_initializer(uid, uuid, room_id, revert_data):
    await session_initializer()
    try:
        await run_single_client(uid, uuid, room_id, revert_data)
    finally:
        await session.close()

async def session_initializer():
    cookies = http.cookies.SimpleCookie()
    cookies["SESSDATA"] = BiliConfig.SESSDATA
    cookies["SESSDATA"]["domain"] = "bilibili.com"

    global session
    session = aiohttp.ClientSession()
    session.cookie_jar.update_cookies(cookies)

async def run_single_client(uid, uuid, room_id, revert_data):
    client = blivedm.BLiveClient(room_id, session=session)
    handler = InitHandler(uid, uuid, room_id, revert_data, client)
    client.set_handler(handler)
    client.start()
    await client.join()
    # await client.stop_and_close()
