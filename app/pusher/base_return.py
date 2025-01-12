from typing import Union
from fastapi import status
from fastapi.responses import JSONResponse, Response

def ret_200(
        data: Union[list, dict, str] | None = {}, 
        message: str="success"
    ) -> Response:

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": 0,
            "message": message,
            "data": data,
        }
    )

def ret_201(
        data: Union[list, dict, str] | None = {}, 
        message: str="parm error"
    ) -> Response:

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": 1001,
            "message": message,
            "data": data,
        }
    )

def ret_202(
        data: Union[list, dict, str] | None = {}, 
        message: str="parm out of range"
    ) -> Response:

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": 1002,
            "message": message,
            "data": data,
        }
    )

def ret_203(
        data: Union[list, dict, str] | None = {}, 
        message: str="not found"
    ) -> Response:

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": 1003,
            "message": message,
            "data": data,
        }
    )

def ret_204(
        data: Union[list, dict, str] | None = {}, 
        message: str=""
    ) -> Response:

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": 1004,
            "message": message,
            "data": data,
        }
    )

def ret_205(
        message: str="server error | parm illegal"
    ) -> Response:

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": 1005,
            "message": message,
            "data": {},
        }
    )

def ret_forbiddent():
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            "code": 1006,
            "message": "no permission to access this router",
            "data": {},
        }
    )

def ret_deprecated():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": 1007,
            "message": "deprecated",
            "data": {},
        }
    )

def ret_temp(
        code: int = -1,
        message: str = "[]"
    ):
    content={
        "code": code,
        "message": message,
        "data": {},
    }
    return content
