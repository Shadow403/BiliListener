from fastapi import APIRouter

from config import Router
from ...base_return import *

from database import *
from database.model import UIDS
from database.connector import get_db_config_session

from ..model.v1._model_listening import get_listening
from ..model.v1._model_uids import get_uids


router = APIRouter(prefix=Router.info_perfix, tags=Router.info_tags)

@router.get("/listening", response_model=get_listening)
async def get_listening_():
    with get_db_config_session() as session:
        uid_query_list = session.query(UIDS.uid).filter(UIDS.is_live == True).all()
        uid_list = [uid[0] for uid in uid_query_list]

    return ret_200(data=uid_list)

@router.get("/uids", response_model=get_uids)
async def get_uids_():
    with get_db_config_session() as session:
        uid_query_list = session.query(UIDS.uid).filter(UIDS.is_ban == False).all()
        uid_list = [uid[0] for uid in uid_query_list]

    return ret_200(data=uid_list)
