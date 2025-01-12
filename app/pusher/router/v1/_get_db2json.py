import os
import json
from fastapi import Query
from typing import Optional
from fastapi import APIRouter

from ...base_return import *
from config import Router, config

from database.model import *
from database.connector import get_db_config_session, get_db_worker_session

from ..model.v1._model_db2json_data import get_data_db2json
from ..model.v1._model_db2json_config import get_config_db2json


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

    json_uid = live_config_data.uid
    json_root = f"{config.json_path}/{json_uid}"
    json_path = f"{json_root}/{live_uuid}_{page}.json"

    if config.json_enable:
        os.makedirs(json_root, exist_ok=True)

    if config.json_enable and os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return ret_translation(data)

    with get_db_worker_session(f"{json_uid}/{live_uuid}") as worker_db_session:
        page = int(page)
        page_size = 1000

        total_logs = worker_db_session.query(LIVE_LOGS).count()
        total_pages = (total_logs + page_size - 1) // page_size

        if page > total_pages:
            return ret_202()

        offset = (page - 1) * page_size
        live_logs = worker_db_session.query(LIVE_LOGS).limit(page_size).offset(offset).all()
        live_logs_json = [x.live_logs_json() for x in live_logs]
        live_logs_json_chunks = [live_logs_json[i:i + 100] for i in range(0, len(live_logs_json), 100)]
        
        live_statistics = worker_db_session.query(LIVE_STATISTICS).filter(LIVE_STATISTICS.uuid == live_uuid).first()
        live_statistics_json = live_statistics.live_statistics_json()

        data = {
            "live_config": {
                "page_current": page,
                "page_lasted": total_pages,
                "base": live_config_data.live_data_json(),
                "statistics": live_statistics_json
            },
            "live_logs": live_logs_json_chunks
        }

        if config.json_enable:
            with open(json_path, "w", encoding="utf-8") as f:
                f.write(json.dumps(
                        ret_200_concatenation(data),
                        indent=4,
                        ensure_ascii=False,
                    )
                )

    return ret_200(data)
