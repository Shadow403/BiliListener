from fastapi import APIRouter

from .utils import *
from config import Router
from ..base_return import *

from database import *
from database.model import UIDS
from database.connector import get_db_config_session


router = APIRouter(prefix=Router.info_perfix, tags=Router.info_tags)

@router.get("/listening")
async def get_listening():
    with get_db_config_session() as session:
        uid_query_list = session.query(UIDS.uid).filter(UIDS.is_live == True).all()
        uid_list = [uid[0] for uid in uid_query_list]

    return ret_200(data=uid_list)

@router.get("/uids")
async def get_uids():
    with get_db_config_session() as session:
        uid_query_list = session.query(UIDS.uid).filter(UIDS.is_ban == True).all()
        uid_list = [uid[0] for uid in uid_query_list]

    return ret_200(data=uid_list)
