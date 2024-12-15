from fastapi import APIRouter

from config import Router
from ..base_return import *

from database import *
from database.model import *
from database.connector import get_db_config_session

from .model._model_edit_add import put_add_uid
from .model._model_del_uid import put_delete_uid


router = APIRouter(prefix=Router.stats_perfix, tags=Router.stats_tags)

@router.get("/total")
async def get_total_():
    with get_db_config_session() as config_db_session:
        total = config_db_session.query(LIVE_DATA).all()
        total_list = [x.live_data_json() for x in total]

        return ret_200(total_list)
