from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from apscheduler.schedulers.background import BackgroundScheduler

from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html
)

from .utils import *
from .base_return import *
from config import config
from .router import MRouter
from .router.model.v1._model_api import get_api
from .utils.tasks import live_status_inspectors, live_clear_inspectors


scheduler = BackgroundScheduler()
scheduler.add_job(live_status_inspectors, "interval", seconds=config.push_query_delay)
scheduler.add_job(live_clear_inspectors, "interval", seconds=config.live_clear_delay)
scheduler.start()

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
    title=config.appname,
    version=config.appver,
    contact=config.ct_info,
    license_info=config.lc_info,
    openapi_url=config.web_oapi,
    description=config.web_desc
)

app.include_router(MRouter)

@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()

@app.get("/", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title,
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url=config.sw_jvs,
        swagger_css_url=config.sw_css,
        swagger_favicon_url=config.sw_ico,
        swagger_ui_parameters={"defaultModelsExpandDepth": -1}
    )

@app.get(config.perfix, tags=config.tags, response_model=get_api)
async def read_root():
    return ret_200(data={
        "server_time": func_time(info=True),
        "server_ntsp": func_time(timestamp=True)
    })

@app.exception_handler(404)
async def custom_http_404_exception_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content=ret_temp(404, "not found"),
    )

@app.exception_handler(RequestValidationError)
async def custom_http_422_exception_handler(request, exc):
    message = exc.__dict__["_errors"][0]["msg"]
    return JSONResponse(
        status_code=422,
        content=ret_temp(422, message)
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content=ret_temp(500, "internal server error")
    )

