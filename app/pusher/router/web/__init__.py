from config import Router
from fastapi import APIRouter

from .hub import router as HubRouter

MRouter = APIRouter(prefix=Router.web_root)

MRouter.include_router(HubRouter)
