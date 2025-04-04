import asyncio
from blivedm import logger
from fastapi import APIRouter, WebSocket

from database.model import *
from config import config, Router
from ....utils._func_time import func_time
from ....base_return import ret_200_concatenation
from database.connector import get_db_config_session

router = APIRouter(prefix=Router.ws_perfix, tags=Router.ws_tags)

@router.websocket("/listening")
async def ws_hub(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            with get_db_config_session() as session:
                uid_query_len = session.query(UIDS.uid).count()
                uid_query_list = session.query(UIDS.uid).filter(UIDS.is_live == True).all()

            time = func_time()
            uid_list = [uid[0] for uid in uid_query_list]

            full_data = ret_200_concatenation({
                "time": time,
                "uids": uid_query_len,
                "uids_listening": uid_list
            })

            await websocket.send_json(full_data)
            await asyncio.sleep(config.ws_listening)

    except Exception as e:
        if config.debug:
            logger.debug(f"Websocket Error: {e}")
        pass
