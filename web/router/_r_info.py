import json
from ..base_return import *
from fastapi import APIRouter
from config import WebAPI, PathConfig

router = APIRouter(prefix=WebAPI.PREFIX)

@router.get("/listening")
async def _r_listening():
    with open(PathConfig.CACHE_Path, "r") as x:
        data = json.load(x)
    listenList = data["data"]["listening"]
    return ret_200(data=listenList)

@router.get("/uids")
async def _r_uids():
    with open(PathConfig.UIDLIST_Path, "r") as x:
        data = json.load(x)
    limit = data["limit"]
    uids = data["data"]["uids"]
    if len(uids) >= limit:
        reach = True
    reach = False
    data = {
        "reach": reach,
        "limit": limit,
        "uids": uids
    }
    return ret_200(data=data)
