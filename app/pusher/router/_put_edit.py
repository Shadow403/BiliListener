from fastapi import APIRouter

from config import Router
from ..base_return import *

from database import *
from database.model import UIDS
from database.connector import get_db_config_session

from .model._model_edit_add import put_add_uid
from .model._model_del_uid import put_delete_uid


router = APIRouter(prefix=Router.edit_perfix, tags=Router.edit_tags)

@router.put("/add/uid/{uid}", response_model=put_add_uid)
async def put_add_uid_(
        uid: int
    ):
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

@router.put("/del/uid/{uid}", response_model=put_delete_uid)
async def put_delete_uid_(
        uid: int
    ):
    with get_db_config_session() as session:
        is_uid_exists = session.query(UIDS).filter(UIDS.uid == uid).first()

        if is_uid_exists:
            session.delete(is_uid_exists)
            session.commit()
            return ret_200(message="deleted")
        else:
            return ret_203(message="uid not exists")

