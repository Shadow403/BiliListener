import json
from ..base_return import *
from fastapi import APIRouter
from config import WebAPI, PathConfig
from ..utils import _read_uidlist, _read_cache

router = APIRouter(prefix=WebAPI.PREFIX)

@router.get("/listening")
async def _r_listening():
    data = await _read_cache()
    listenList = data["data"]["listening"]
    return ret_200(data=listenList)

@router.get("/uids")
async def _r_uids():
    data = await _read_uidlist()
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
