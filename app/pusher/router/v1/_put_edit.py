from fastapi import Request
from fastapi import APIRouter

from ...base_return import *
from config import Router, config

from database import *
from database.model import UIDS
from database.connector import get_db_config_session

from ..model.v1._model_edit_add import put_add_uid
from ..model.v1._model_edit_del import put_delete_uid


router = APIRouter(prefix=Router.edit_perfix, tags=Router.edit_tags)

@router.put("/add/uid/{uid}", response_model=put_add_uid, deprecated=True)
async def put_add_uid_(
        uid: int,
        request: Request
    ):
    """
    ### 添加uid
    - **uid** - 要添加的uid
    """
    if request.client.host not in config.acc_put_uid and config.strict:
        return ret_forbiddent()

    with get_db_config_session() as session:
        is_uid_exists = session.query(UIDS).filter(UIDS.uid == uid).first()

        if is_uid_exists:
            return ret_203(message="uid already exists")
        else:
            new_uid = UIDS(
                    uid=uid,
                    is_live=False,
                    is_ban=False
                )
            session.add(new_uid)
            session.commit()
            return ret_200(message="added")

@router.put("/del/uid/{uid}", response_model=put_delete_uid, deprecated=True)
async def put_delete_uid_(
        uid: int,
        request: Request
    ):
    """
    ### 删除uid
    - **uid** - 要删除的uid
    """
    if request.client.host not in config.acc_put_uid and config.strict:
        return ret_forbiddent()

    with get_db_config_session() as session:
        is_uid_exists = session.query(UIDS).filter(UIDS.uid == uid).first()

        if is_uid_exists:
            session.delete(is_uid_exists)
            session.commit()
            return ret_200(message="deleted")
        else:
            return ret_203(message="uid not exists")

