import aiohttp
import http.cookies
from typing import Optional
from modules import blivedm
from .handle import InitHandler
from config.config import BiliConfig

session: Optional[aiohttp.ClientSession] = None

async def main(uid, room_id, db_session):
    await init_session()
    try:
        await run_single_client(uid, room_id, db_session)
    finally:
        await session.close()

async def init_session():
    cookies = http.cookies.SimpleCookie()
    cookies["SESSDATA"] = BiliConfig.SESSDATA
    cookies["SESSDATA"]["domain"] = "bilibili.com"

    global session
    session = aiohttp.ClientSession()
    session.cookie_jar.update_cookies(cookies)

async def run_single_client(uid, room_id, db_session):
    w_client = blivedm.BLiveClient(room_id, session=session)
    handler = InitHandler(uid, room_id, db_session, w_client)
    w_client.set_handler(handler)
    w_client.start()
    await w_client.join()
