from config import WebAPI
from fastapi import APIRouter

from ._get_info import router as get_info_router
from ._put_edit import router as put_edit_router
from ._get_db2json import router as get_db2json_router

MRouter = APIRouter(prefix=WebAPI.PREFIX)

MRouter.include_router(get_info_router)
MRouter.include_router(put_edit_router)
MRouter.include_router(get_db2json_router)
