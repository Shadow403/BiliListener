from config import Router
from fastapi import APIRouter

from ._get_hub import router as _get_hub_router
from ._put_edit import router as put_edit_router
from ._get_db2json import router as get_db2json_router

MRouter = APIRouter(prefix=Router.v2_root)

MRouter.include_router(_get_hub_router)
MRouter.include_router(put_edit_router)
MRouter.include_router(get_db2json_router)
