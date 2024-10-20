import json
from ..base_return import *
from fastapi import APIRouter
from config import WebAPI, PathConfig

router = APIRouter(prefix=WebAPI.PREFIX)

@router.get("/add/uid/{uid}")
async def _r_add(uid):
    if not uid.isdigit() or uid == "":
        return ret_200(message="uid must be number")
    uid = int(uid)
    with open(PathConfig.UIDLIST_Path, "r") as x:
        data = json.load(x)
    uidlist = data["data"]["uids"]
    if uid in uidlist:
        return ret_200(message="uid already exist")
    uidlist.append(uid)
    with open(PathConfig.UIDLIST_Path, "w") as x:
        json.dump(data, x, ensure_ascii=False, indent=4)
    return ret_200(message="added")

@router.get("/del/uid/{uid}")
async def _r_del(uid):
    if not uid.isdigit() or uid == "":
        return ret_200(message="uid must be number")
    uid = int(uid)
    with open(PathConfig.UIDLIST_Path, "r") as x:
        data = json.load(x)
    uidlist = data["data"]["uids"]
    if uid not in uidlist:
        return ret_200(message="uid not exist")
    uidlist.remove(uid)
    with open(PathConfig.UIDLIST_Path, "w") as x:
        json.dump(data, x, ensure_ascii=False, indent=4)
    return ret_200(message="deleted")
