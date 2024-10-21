from config import WebAPI
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from .base_return import *
from .utils import _nowtime

from .router._r_info import router as _r_info
from .router._r_edit import router as _r_edit
from .router._r_db2json import router as _r_db2json

app = FastAPI()

app.include_router(_r_info)
app.include_router(_r_edit)
app.include_router(_r_db2json)

@app.get("/")
async def read_root():
    return ret_200(data={
        "server_time": await _nowtime(info=True),
        "server_ntsp": await _nowtime(timestamp=True)
    })

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=WebAPI._c_404,
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=WebAPI._c_500,
    )
