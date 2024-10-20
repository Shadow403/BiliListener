import time
import json
from modules import blivedm
from config import PathConfig
from config import BiliConfig
from modules.log import logger
from ..database.model import _init_
from modules.blivedm.models import web as web_models

_c_et: int = 0
_c_dm: int = 0
_c_gf: int = 0
_c_gd: int = 0
_c_sc: int = 0
_c_pc: int = 0

class InitHandler(blivedm.BaseHandler):
    def __init__(self, uid, room_id, db_session, work_client):
        self.uid = uid
        self.room_id = room_id
        self.session = db_session
        self.init_stsp = int(time.time())
        self.work_client = work_client

    def _on_heartbeat(self, client: blivedm.BLiveClient, message: web_models.HeartbeatMessage):
        logger.info(f"[WORKER] [{client.room_id}] HB POPPING")

    def _on_interact_word(self, client: blivedm.BLiveClient, message: web_models.EnterMessage):
        self.session.add(
            _init_(
                    type=BiliConfig._et, 
                    name=message.uname, 
                    uid=message.uid, 
                    tsp=message.timestamp
                )
            )
        self.session.commit()
        global _c_et
        _c_et += 1
        logger.info(f"[WORKER] [{client.room_id}] {message.uname}({message.uid}) 进入房间")

    def _on_danmaku(self, client: blivedm.BLiveClient, message: web_models.DanmakuMessage):
        self.session.add(
            _init_(
                    type=BiliConfig._dm, 
                    name=message.uname, 
                    message = message.msg,
                    uid=message.uid, 
                    tsp=message.timestamp
                )
            )
        self.session.commit()
        global _c_dm
        _c_dm += 1
        logger.info(f"[WORKER] [{client.room_id}] {message.uname}: {message.msg}")

    def _on_gift(self, client: blivedm.BLiveClient, message: web_models.GiftMessage):
        t_coin = message.coin_type
        price = message.total_coin
        self.session.add(
            _init_(
                type=BiliConfig._gf, 
                coin_type=message.coin_type, 
                name=message.uname, 
                uid=message.uid, 
                gift_id = message.gift_id,
                gift_name = message.gift_name,
                price=price, 
                count=message.num, 
                tsp=message.timestamp
            )
        )
        self.session.commit()
        global _c_gf, _c_pc
        _c_gf += 1
        if t_coin == "gold":
            _c_pc += price
        logger.info(f"[WORKER] [{client.room_id}] {message.uname} 赠送 {message.gift_name}x{message.num}"
              f" ({t_coin}瓜子x{price})")

    def _on_buy_guard(self, client: blivedm.BLiveClient, message: web_models.GuardBuyMessage):
        price = message.price
        self.session.add(
            _init_(
                type=BiliConfig._gd, 
                name=message.username, 
                uid=message.uid, 
                gift_name = message.guard_level,
                price=price, 
                count=message.num, 
                tsp=message.start_time
            )
        )
        self.session.commit()
        global _c_gd, _c_pc
        _c_gd += 1
        _c_pc += price
        logger.info(f"[WORKER] [{client.room_id}] {message.username} 购买 {message.gift_name}")

    def _on_super_chat(self, client: blivedm.BLiveClient, message: web_models.SuperChatMessage):
        price = message.price * 1000
        self.session.add(
            _init_(
                type=BiliConfig._sc, 
                name=message.uname, 
                uid=message.uid, 
                message = message.message,
                price=price, 
                # 价格统一 1¥ = 1000c
                tsp=message.start_time
            )
        )
        self.session.commit()
        global _c_sc, _c_pc
        _c_sc += 1
        _c_pc += price
        logger.info(f"[WORKER] [{client.room_id}] 醒目留言 {message.price}¥ {message.uname}: {message.message}")

    def _on_preparing(self, client: blivedm.BLiveClient, message: web_models.PreparingMessage):
        etsp = int(time.time())
        config = f"{PathConfig.DATA_Path}/{self.uid}/config.json"
        with open(config, "r") as x:
            data = json.load(x)

        last_key = str(int(list(data["data"].keys())[-1])+1)
        data["etsp"] = etsp
        data["data"][last_key] = {
            "stsp": self.init_stsp,
            "etsp": etsp,
            "total": {
                "_et": _c_et,
                "_dm": _c_dm,
                "_gf": _c_gf,
                "_gd": _c_gd,
                "_sc": _c_sc,
                "_pc": _c_pc
            }
        }
        with open(config, "w") as x:
            json.dump(data, x, ensure_ascii=False, indent=4)

        logger.warning(f"[WORKER] [{client.room_id}] 房间下播，停止接收消息")
        self.work_client.stop()
