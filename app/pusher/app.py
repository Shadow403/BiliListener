from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from apscheduler.schedulers.background import BackgroundScheduler
from starlette.exceptions import HTTPException as StarletteHTTPException

from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html
)

from .utils import *
from .base_return import *
from .router import MRouter
from config import WebAPI, Router, BiliConfig
from .utils.tasks import live_status_inspectors
from database.connector import config_database_init


_openapi = FastAPI.openapi
def openapi(self: FastAPI):
    _openapi(self)
    for _, method_item in self.openapi_schema.get("paths").items():
        for _, param in method_item.items():
            responses = param.get("responses")
            if "422" in responses:
                del responses["422"]
    return self.openapi_schema
FastAPI.openapi = openapi

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    title=WebAPI.APPNAME,
    version=WebAPI.APPVER,
    contact=WebAPI.ct_info,
    license_info=WebAPI.lc_info,
    openapi_url=WebAPI.web_oapi,
    description=WebAPI.web_desc
)

app.include_router(MRouter)
db_session = config_database_init()

scheduler = BackgroundScheduler()
scheduler.add_job(live_status_inspectors, "interval", seconds=BiliConfig.QUERYDELAY)
scheduler.start()

@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()

@app.get("/", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title,
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url=WebAPI.sw_jvs,
        swagger_css_url=WebAPI.sw_css,
        swagger_favicon_url=WebAPI.sw_ico,
        swagger_ui_parameters={"defaultModelsExpandDepth": -1}
    )

@app.get(Router.api_perfix, tags=Router.api_tags)
async def read_root():
    return ret_200(data={
        "server_time": func_time(info=True),
        "server_ntsp": func_time(timestamp=True)
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

