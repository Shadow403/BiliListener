from config import Router
from fastapi import APIRouter

from .ws_hub import router as ws_hub_router
from .ws_listening import router as ws_listening_router

MRouter = APIRouter(prefix=Router.ws_v1_root)

MRouter.include_router(ws_hub_router)
MRouter.include_router(ws_listening_router)

