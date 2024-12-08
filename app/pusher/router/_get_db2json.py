from config import Router
from ..base_return import *
from fastapi import APIRouter

router = APIRouter(prefix=Router.livelogs_perfix, tags=Router.livelogs_tags)

@router.get("/data/{uid}")
async def get_live_config(uid):
    pass

@router.get("/data/{live_uuid}")
async def get_live_logs(live_uuid):
    pass
