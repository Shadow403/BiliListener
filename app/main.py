import time
import json
import multiprocessing
from modules.log import logger
from .worker import init_listen
from .pusher import _get_uid_rid
from config import BiliConfig, PathConfig

CACHE_Path = PathConfig.CACHE_Path

def main():
    with open(CACHE_Path, "r") as x:
        cache = json.load(x)
    if cache["data"]["listening"] != []:
        with open(CACHE_Path, "w") as x:
            cache["data"]["listening"] = []
            json.dump(cache, x, ensure_ascii=False, indent=4)

    while True:
        with open(PathConfig.UIDLIST_Path, "r") as x:
            uid_list = json.load(x)

        if uid_list["status"] != True:
            logger.critical(f"[MAIN_LISTENER] 未开启监听")
            break

        logger.success("[MAIN_LISTENER] 正在监听")
        rList = _get_uid_rid(uid_list["data"])
        if rList == []:
            continue
        with open(CACHE_Path, "r") as x:
            cache = json.load(x)
        listening_0 = cache["data"]["listening"]
        listening_1 = []

        for Linfo in rList:
            uid = Linfo[0]
            rid = Linfo[1]
            listening_1.append(uid)
            if uid in listening_0:
                continue
            logger.success(f"[MAIN_LISTENER] 开始监听 {uid} ({rid})")
            p = multiprocessing.Process(target=init_listen, args=(uid, rid))
            p.start()
        with open(CACHE_Path, "r") as x:
            cache = json.load(x)
        with open(CACHE_Path, "w") as x:
            cache["data"]["listening"] = listening_1
            json.dump(cache, x, ensure_ascii=False, indent=4)

        time.sleep(BiliConfig.QUERYDELAY)
