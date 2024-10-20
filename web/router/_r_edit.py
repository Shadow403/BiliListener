import json
from ..base_return import *
from fastapi import APIRouter
from config import WebAPI, PathConfig
from ..utils import _parmTest, _read_uidlist

router = APIRouter(prefix=WebAPI.PREFIX)

@router.get("/add/uid/{uid}")
async def _r_add(uid):
    tParm = await _parmTest(uid)
    if tParm != True:
        return tParm
    uid = int(uid)
    data = await _read_uidlist()
    uidlist = data["data"]["uids"]
    if uid in uidlist:
        return ret_203(message="uid already exist")
    uidlist.append(uid)
    with open(PathConfig.UIDLIST_Path, "w") as x:
        json.dump(data, x, ensure_ascii=False, indent=4)
    return ret_200(message="added")

@router.get("/del/uid/{uid}")
async def _r_del(uid):
    tParm = await _parmTest(uid)
    if tParm != True:
        return tParm
    uid = int(uid)
    data = await _read_uidlist()
    uidlist = data["data"]["uids"]
    if uid not in uidlist:
        return ret_203(message="uid not exist")
    uidlist.remove(uid)
    with open(PathConfig.UIDLIST_Path, "w") as x:
        json.dump(data, x, ensure_ascii=False, indent=4)
    return ret_200(message="deleted")
