from sqlalchemy import func
from fastapi import APIRouter
from database.model import UIDS, LIVE_DATA
from database.connector import get_db_config_session

from config import Router
from ...base_return import ret_200
from ...utils._func_time import func_time
from ..model.v2._model_get_hub import get_hub

router = APIRouter(prefix=Router.web_perfix, tags=Router.web_tags)

@router.get("/hub", response_model=get_hub)
async def get_hub():
    with get_db_config_session() as session:
        uids_count = len(session.query(UIDS.uid).all())
        live_count = len(session.query(LIVE_DATA).all())
        uids_listening_count = len(session.query(UIDS.uid).filter(UIDS.is_live == True).all())

        gf, et, gd, dm, sc = session.query(
            func.sum(LIVE_DATA.all_gift).label('total_gift'),
            func.sum(LIVE_DATA.all_enter).label('total_enter'),
            func.sum(LIVE_DATA.all_guard).label('total_guard'),
            func.sum(LIVE_DATA.all_danmaku).label('total_danmaku'),
            func.sum(LIVE_DATA.all_superchat).label('total_superchat')
        ).first()

    total_data = {
        "gift": gf,
        "enter": et,
        "guard": gd,
        "danmaku": dm,
        "superchat": sc
    }

    total_data = {
        k: (v if v is not None else 0) for k, 
        v in total_data.items()}

    full_data = ret_200({
        "time": func_time(),
        "uids": uids_count,
        "uids_listening": uids_listening_count,
        "live_count": live_count,
        "total": total_data
    })

    return full_data
