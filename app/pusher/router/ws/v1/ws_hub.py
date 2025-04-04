import asyncio
from blivedm import logger
from sqlalchemy import func
from fastapi import APIRouter, WebSocket

from database.model import *
from config import config, Router
from ....utils._func_time import func_time
from ....base_return import ret_200_concatenation
from database.connector import get_db_config_session

router = APIRouter(prefix=Router.ws_perfix, tags=Router.ws_tags)

@router.websocket("/hub")
async def ws_hub(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            with get_db_config_session() as session:
                uids_count = session.query(UIDS.uid).count()
                live_count = session.query(LIVE_DATA).count()
                uids_listening_count = len(session.query(UIDS.uid).filter(UIDS.is_live == True).all())

                gf, et, gd, dm, sc = session.query(
                    func.sum(LIVE_DATA.all_gift).label("total_gift"),
                    func.sum(LIVE_DATA.all_enter).label("total_enter"),
                    func.sum(LIVE_DATA.all_guard).label("total_guard"),
                    func.sum(LIVE_DATA.all_danmaku).label("total_danmaku"),
                    func.sum(LIVE_DATA.all_superchat).label("total_superchat")
                ).first()

            total_data = {
                "gift": gf,
                "enter": et,
                "guard": gd,
                "danmaku": dm,
                "superchat": sc
            }

            total_data = {
                k: (v if v is not None else 0) for k, 
                v in total_data.items()
            }

            full_data = ret_200_concatenation({
                "time": func_time(),
                "uids": uids_count,
                "uids_listening": uids_listening_count,
                "live_count": live_count,
                "total": total_data
            })
            await websocket.send_json(full_data)
            await asyncio.sleep(config.ws_hub)

    except Exception as e:
        if config.debug:
            logger.debug(f"Websocket Error: {e}")
        pass
