from fastapi import APIRouter

from .utils import *
from config import Router
from ..base_return import *

from database import *
from database.model import UIDS
from database.connector import get_db_config_session

router = APIRouter(prefix=Router.edit_perfix, tags=Router.edit_tags)

@router.put("/add/uid/{uid}")
async def put_add_uid(uid):
    if parm_type_int(uid):
        with get_db_config_session() as session:
            is_uid_exists = session.query(UIDS).filter(UIDS.uid == uid).first()

            if is_uid_exists:
                return ret_203(message="uid already exists")
            else:
                new_uid = UIDS(
                        uid=uid,
                        is_live = 0,
                        is_ban = 0
                    )
                session.add(new_uid)
                session.commit()
                return ret_200(message="added")
    return ret_203(message="uid is not int")

@router.put("/del/uid/{uid}")
async def put_delete_uid(uid):
    if parm_type_int(uid):
        with get_db_config_session() as session:
            is_uid_exists = session.query(UIDS).filter(UIDS.uid == uid).first()

            if is_uid_exists:
                session.delete(is_uid_exists)
                session.commit()
                return ret_200(message="deleted")
            else:
                return ret_203(message="uid not exists")
    return ret_203(message="uid is not int")

