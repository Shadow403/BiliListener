import sys
import blivedm
from blivedm.log import logger
from blivedm.models import web as web_models

from .database.data_handle import data_commit_handle


class InitHandler(blivedm.BaseHandler):
    def __init__(s, uid, uuid, rid, rd, wc):
        s.uid = uid
        s.rid = rid
        s.uuid = uuid
        s.wc = wc
        s.rd = rd
        s.dbh = data_commit_handle(uid, uuid)

    def _on_heartbeat(s, client: blivedm.BLiveClient, message: web_models.HeartbeatMessage):
        logger.warning(f"[HB] POPPING & COMMIT DATA")
        s.dbh.data_commit(s.rd)

    def _on_interact_word(s, client: blivedm.BLiveClient, message: web_models.EnterMessage):
        logger.info(f"[ET] {message.uname}({message.uid}) 进入房间")
        s.rd.all_enter += 1
        s.dbh.data_enter(message)

    def _on_danmaku(s, client: blivedm.BLiveClient, message: web_models.DanmakuMessage):
        logger.info(f"[DM] {message.uname}({message.uid}): {message.msg}")
        s.rd.all_danmaku += 1
        s.dbh.data_danmaku(message)

    def _on_gift(s, client: blivedm.BLiveClient, message: web_models.GiftMessage):
        logger.info(f"[GF] {message.uname} 赠送 {message.gift_name}x{message.num}"
              f" ({message.coin_type}瓜子x{message.total_coin})")
        s.rd.all_gift += 1
        s.dbh.data_gift(message)

    def _on_buy_guard(s, client: blivedm.BLiveClient, message: web_models.GuardBuyMessage):
        logger.info(f"[GD] {message.username} 购买 {message.gift_name}")
        s.rd.all_guard += 1
        s.dbh.data_guard(message)

    def _on_super_chat(s, client: blivedm.BLiveClient, message: web_models.SuperChatMessage):
        logger.info(f"[SC] {message.price}¥ {message.uname}: {message.message}")
        s.rd.all_superchat += 1
        s.dbh.data_superchat(message)

    def _on_preparing(s, client: blivedm.BLiveClient, message: web_models.PreparingMessage):
        logger.warning(f"[END] [{s.rid}] 房间下播，停止接收消息")
        s.dbh.data_commit(s.rd)
        s.dbh.data_finish(s.rd)
        s.wc.stop()
        sys.exit()
