from fastapi import Query
from typing import Optional
from fastapi import APIRouter

from config import Router
from ..base_return import *

from database import *
from database.model import *
from database.connector import get_db_config_session, get_db_worker_session

from .model._model_db2json_data import get_data_db2json
from .model._model_db2json_config import get_config_db2json


router = APIRouter(prefix=Router.livelogs_perfix, tags=Router.livelogs_tags)

@router.get("/config/{uid}", response_model=get_config_db2json)
async def get_live_config(
        uid: str
    ):
    with get_db_config_session() as config_db_session:
        live_config_data = config_db_session.query(LIVE_DATA).filter(
                LIVE_DATA.uid == uid
            ).all()

        if live_config_data:
            live_config_data_json = [x.live_data_json() for x in live_config_data]

            full_data = {
                "uid": uid,
                "live_count": len(live_config_data_json),
                "live_config": live_config_data_json
            }

            return ret_200(full_data)
        return ret_203(message="no target uid live data")

@router.get("/data/{live_uuid}", response_model=get_data_db2json)
async def get_live_logs(
        live_uuid: str, 
        page: Optional[int] = Query(1, description="页数")
    ):

    with get_db_config_session() as config_db_session:
            live_config_data = config_db_session.query(LIVE_DATA).filter(
                LIVE_DATA.uuid == live_uuid
            ).first()

    if not live_config_data:
        return ret_203(message="uuid not exists")

    with get_db_worker_session(f"{live_config_data.uid}/{live_uuid}") as worker_db_session:
        page = int(page)
        page_size = 1000
        offset = (page - 1) * page_size
        live_logs = worker_db_session.query(LIVE_LOGS).limit(page_size).offset(offset).all()
        live_logs_json = [x.live_logs_json() for x in live_logs]
        live_logs_json_chunks = [live_logs_json[i:i + 100] for i in range(0, len(live_logs_json), 100)]
        
        live_statistics = worker_db_session.query(LIVE_STATISTICS).filter(LIVE_STATISTICS.uuid == live_uuid).first()
        live_statistics_json = live_statistics.live_statistics_json()

        total_logs = worker_db_session.query(LIVE_LOGS).count()
        total_pages = (total_logs + page_size - 1) // page_size

        full_data = {
            "live_config": {
                    "now": page,
                    "page": total_pages,
                    "base": live_config_data.live_data_json(),
                    "statistics": live_statistics_json
                },
            "live_logs": live_logs_json_chunks
        }

        return ret_200(full_data)
