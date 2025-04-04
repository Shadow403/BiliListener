import blivedm
from blivedm.log import logger
from blivedm.models import web as web_models

from .database.data_handle import data_commit_handle


class InitHandler(blivedm.BaseHandler):
    def __init__(self, live_config, debug, client):
        super().__init__()
        self.debug = debug
        self.client = client
        self.uid = live_config.uid
        self.rid = live_config.rid
        self.uuid = live_config.uuid
        self.rd = live_config.revert_data
        self.dbh = data_commit_handle(self.uid, self.uuid)

    def _on_heartbeat(self, client: blivedm.BLiveClient, message: web_models.HeartbeatMessage):
        # logger.warning(f"[HB] POPPING & COMMIT DATA")
        self.dbh.data_commit(self.rd)

    def _on_interact_word(self, client: blivedm.BLiveClient, message: web_models.InteractWordMessage):
        # logger.info(f"[ET] {message.uname}({message.uid}) 进入房间")
        self.rd.all_enter += 1
        self.dbh.data_enter(message)

    def _on_danmaku(self, client: blivedm.BLiveClient, message: web_models.DanmakuMessage):
        # logger.info(f"[DM] {message.uname}({message.uid}): {message.msg}")
        self.rd.all_danmaku += 1
        self.dbh.data_danmaku(message)

    def _on_gift(self, client: blivedm.BLiveClient, message: web_models.GiftMessage):
        # logger.info(f"[GF] {message.uname} 赠送 {message.gift_name}x{message.num}"
        #      f" ({message.coin_type}瓜子x{message.total_coin})")
        self.rd.all_gift += message.num

        if message.coin_type == "gold":
            self.rd.gold_gift += message.num
            self.rd.all_price += message.total_coin * message.num
        else:
            self.rd.silver_gift += message.num

        self.dbh.data_gift(message)

    def _on_buy_guard(self, client: blivedm.BLiveClient, message: web_models.GuardBuyMessage):
        # logger.info(f"[GD] {message.username} 购买 {message.gift_name}")
        self.rd.all_guard += message.num
        self.rd.all_price += message.price * message.num
        self.dbh.data_guard(message)

    def _on_super_chat(self, client: blivedm.BLiveClient, message: web_models.SuperChatMessage):
        # logger.info(f"[SC] {message.price}¥ {message.uname}: {message.message}")
        self.rd.all_superchat += 1
        self.rd.all_price += message.price * 1000
        self.dbh.data_superchat(message)

    def _on_preparing(self, client: blivedm.BLiveClient, message: web_models.PreparingMessage):
        logger.warning(f"[END] [{self.uid}({self.rid})] 房间下播，停止接收消息")
        self.dbh.data_commit(self.rd)
        self.dbh.data_finish(self.rd)
        self.client.stop()
        # await self.client.stop_and_close()
