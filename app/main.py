import time
import json
import multiprocessing
from config import BiliConfig
from modules.log import logger
from .worker import init_listen
from .pusher import _get_uid_rid
from .utils import _r_read_cache, _r_read_uidlist

async def main():
    cache_path, cache = await _r_read_cache()
    if cache["data"]["listening"] != []:
        with open(cache_path, "w") as x:
            cache["data"]["listening"] = []
            json.dump(cache, x, ensure_ascii=False, indent=4)

    while True:
        cache_path, uid_list = await _r_read_uidlist()
        if uid_list["status"] != True:
            logger.critical(f"[MAIN_LISTENER] 未开启监听")
            break

        logger.success("[MAIN_LISTENER] 正在监听")
        rList = await _get_uid_rid(uid_list["data"])
        if rList == []:
            time.sleep(BiliConfig.QUERYDELAY)
            continue
        cache_path, cache = await _r_read_cache()
        listening_0 = cache["data"]["listening"]
        listening_1 = []

        for Linfo in rList:
            uid = Linfo[0]
            rid = Linfo[1]
            livetime = Linfo[2]
            listening_1.append(uid)
            if uid in listening_0:
                continue
            logger.success(f"[MAIN_LISTENER] 开始监听 {uid} ({rid})")
            p = multiprocessing.Process(target=init_listen, args=(uid, rid, livetime))
            p.start()
        with open(cache_path, "w") as x:
            cache["data"]["listening"] = listening_1
            json.dump(cache, x, ensure_ascii=False, indent=4)

        time.sleep(BiliConfig.QUERYDELAY)
