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
_init_commit: bool = False

def _commit_callback(data):
    global _init_commit
    global _c_et, _c_dm, _c_gf, _c_gd, _c_sc, _c_pc
    if _init_commit == False:
        _c_et += data["_et"]
        _c_dm += data["_dm"]
        _c_gf += data["_gf"]
        _c_gd += data["_gd"]
        _c_sc += data["_sc"]
        _c_pc += data["_pc"]

        _init_commit = True

def _commit_total(init_stsp, total, lost):
    if lost == True:
        etsp = int(time.time())
        livedata_path, data = total
        _commit_callback(data["data"][str(init_stsp)]["total"])
        data["etsp"] = etsp
        data["data"][str(init_stsp)] = {
            "stsp": init_stsp,
            "etsp": etsp,
            "lost": lost,
            "total": {
                "_et": _c_et,
                "_dm": _c_dm,
                "_gf": _c_gf,
                "_gd": _c_gd,
                "_sc": _c_sc,
                "_pc": _c_pc
            }
        }
        with open(livedata_path, "w") as x:
            json.dump(data, x, ensure_ascii=False, indent=4)

    etsp = int(time.time())
    livedata_path, data = total
    data["etsp"] = etsp
    data["data"][str(init_stsp)] = {
        "stsp": init_stsp,
        "etsp": etsp,
        "lost": lost,
        "total": {
            "_et": _c_et,
            "_dm": _c_dm,
            "_gf": _c_gf,
            "_gd": _c_gd,
            "_sc": _c_sc,
            "_pc": _c_pc
        }
    }
    with open(livedata_path, "w") as x:
        json.dump(data, x, ensure_ascii=False, indent=4)

class InitHandler(blivedm.BaseHandler):
    def __init__(self, uid, room_id, total, lost, livetime, db_session, work_client):
        self.uid = uid
        self.room_id = room_id
        self.lost = lost
        self.total = total
        self.session = db_session
        self.init_stsp = livetime
        self.work_client = work_client

    def _on_heartbeat(self, client: blivedm.BLiveClient, message: web_models.HeartbeatMessage):
        logger.info(f"[WORKER] [{client.uid}] HB POPPING")
        _commit_total(self.init_stsp, self.total, self.lost)

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
        logger.info(f"[WORKER] [{client.uid}] {message.uname}({message.uid}) 进入房间")

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
        logger.info(f"[WORKER] [{client.uid}] {message.uname}: {message.msg}")

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
        logger.info(f"[WORKER] [{client.uid}] {message.uname} 赠送 {message.gift_name}x{message.num}"
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
        logger.info(f"[WORKER] [{client.uid}] {message.username} 购买 {message.gift_name}")

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
        logger.info(f"[WORKER] [{client.uid}] 醒目留言 {message.price}¥ {message.uname}: {message.message}")

    def _on_preparing(self, client: blivedm.BLiveClient, message: web_models.PreparingMessage):
        _commit_total(self.init_stsp, self.total, self.lost)
        logger.warning(f"[WORKER] [{client.uid}] [{self.room_id}] 房间下播，停止接收消息")
        self.work_client.stop()
