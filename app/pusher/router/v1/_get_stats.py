from sqlalchemy import func
from fastapi import APIRouter

from config import Router
from ...base_return import *

from database import *
from database.model import *
from database.connector import get_db_config_session

from ..model.v1._model_total import get_total

router = APIRouter(prefix=Router.stats_perfix, tags=Router.stats_tags)

@router.get("/total", response_model=get_total)
async def get_total_():
    """
    ### 获取统计数据
    """
    with get_db_config_session() as config_db_session:
        count = len(config_db_session.query(LIVE_DATA).filter(LIVE_DATA.end_timestamp != 0).all())

        gf, et, gd, dm, sc = config_db_session.query(
            func.sum(LIVE_DATA.all_gift).label('total_gift'),
            func.sum(LIVE_DATA.all_enter).label('total_enter'),
            func.sum(LIVE_DATA.all_guard).label('total_guard'),
            func.sum(LIVE_DATA.all_danmaku).label('total_danmaku'),
            func.sum(LIVE_DATA.all_superchat).label('total_superchat')
        ).first()

        full_data = {
            "count": count,
            "total": {
                "gift": gf,
                "enter": et,
                "guard": gd,
                "danmaku": dm,
                "superchat": sc
            }
        }

        return ret_200(full_data)
