import sys
import blivedm
from blivedm.log import logger
from blivedm.models import web as web_models

from database.model import *
from database.connector import get_db_worker_session

from .database.data_handle import data_handle_v1


class InitHandler(blivedm.BaseHandler):
    def __init__(M, uid, uuid, room_id, revert_data, work_client):
        M.uid = uid
        M.uuid = uuid
        M.room_id = room_id
        M.work_client = work_client
        M.revert_data = revert_data
        with get_db_worker_session(f"{uid}/{uuid}") as db:
            M.db_handle = data_handle_v1(db, M.uuid)

    def _on_heartbeat(M, client: blivedm.BLiveClient, message: web_models.HeartbeatMessage):
        logger.info(f"[HEART] POPPING & COMMIT DATA")
        M.db_handle.data_commit(M.revert_data)

    def _on_interact_word(M, client: blivedm.BLiveClient, message: web_models.EnterMessage):
        logger.info(f"[ET] {message.uname}({message.uid}) 进入房间")
        M.revert_data.all_enter += 1
        M.db_handle.data_enter(message)

    def _on_danmaku(M, client: blivedm.BLiveClient, message: web_models.DanmakuMessage):
        logger.info(f"[DM] {message.uname}({message.uid}): {message.msg}")
        M.revert_data.all_danmaku += 1
        M.db_handle.data_danmaku(message)

    def _on_gift(M, client: blivedm.BLiveClient, message: web_models.GiftMessage):
        logger.info(f"[GF] {message.uname} 赠送 {message.gift_name}x{message.num}"
              f" ({message.coin_type}瓜子x{message.total_coin})")
        M.revert_data.all_gift += 1
        M.db_handle.data_gift(message)

    def _on_buy_guard(M, client: blivedm.BLiveClient, message: web_models.GuardBuyMessage):
        logger.info(f"[GD] {message.username} 购买 {message.gift_name}")
        M.revert_data.all_guard += 1
        M.db_handle.data_guard(message)

    def _on_super_chat(M, client: blivedm.BLiveClient, message: web_models.SuperChatMessage):
        logger.info(f"[SC] {message.price}¥ {message.uname}: {message.message}")
        M.revert_data.all_superchat += 1
        M.db_handle.data_superchat(message)

    def _on_preparing(M, client: blivedm.BLiveClient, message: web_models.PreparingMessage):
        logger.warning(f"[END] [{M.room_id}] 房间下播，停止接收消息")
        M.db_handle.data_commit(M.revert_data)
        M.db_handle.data_finish()
        M.work_client.stop()
        sys.exit()
