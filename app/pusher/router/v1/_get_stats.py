from fastapi import Query
from typing import Optional
from sqlalchemy import func
from fastapi import APIRouter

from config import Router
from ...base_return import *

from database import *
from database.model import *
from database.connector import get_db_config_session

from ..model.v1._model_rank import get_rank
from ..model.v1._model_total import get_total


count_limit = 50
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

@router.get("/main", response_model=get_rank)
async def get_rank_main(
        type: Optional[int] = Query(1, description="排序类型")
    ):
    """
    ### 获取排行榜
    - **type**: 排序类型
      - 1: 入场排行
      - 2: 收入排行
      - 3: 弹幕排行
      - 4: 上舰排行
      - 5: 直播完整
      - 6: 开播时间
    """
    with get_db_config_session() as session:
        if type == 1:
            rank_query = session.query(LIVE_DATA).order_by(LIVE_DATA.all_enter.desc()).limit(count_limit).all()
        elif type == 2:
            rank_query = session.query(LIVE_DATA).order_by(LIVE_DATA.all_price.desc()).limit(count_limit).all()
        elif type == 3:
            rank_query = session.query(LIVE_DATA).order_by(LIVE_DATA.all_danmaku.desc()).limit(count_limit).all()
        elif type == 4:
            rank_query = session.query(LIVE_DATA).order_by(LIVE_DATA.all_guard.desc()).limit(count_limit).all()
        elif type == 5:
            rank_query = session.query(LIVE_DATA).limit(count_limit).all()
        elif type == 6:
            rank_query = session.query(LIVE_DATA).limit(count_limit).all()
        else:
            return ret_205("return parm[type] error")

        rank_dict_list = [rank.live_data_dict() for rank in rank_query]

    full_data = {
        "count": len(rank_dict_list),
        "live_config_list": rank_dict_list
    }

    return ret_200(full_data)
