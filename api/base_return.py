from fastapi import status
from fastapi.responses import JSONResponse, Response  
from typing import Union

def ret_200(*, data: Union[list, dict, str] | None = {}, message: str="success") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": 0,
            "message": message,
            "data": data,
        }
    )

def ret_201(*, data: Union[list, dict, str] | None = {}, message: str="parm error") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": 1001,
            "message": message,
            "data": data,
        }
    )

def ret_202(*, data: Union[list, dict, str] | None = {}, message: str="parm out of range") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": 1002,
            "message": message,
            "data": data,
        }
    )

def ret_203(*, data: Union[list, dict, str] | None = {}, message: str="message return []") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": 1003,
            "message": message,
            "data": data,
        }
    )

def ret_400(*, data: dict = {}, message: str="bad request") -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "code": 400,
            "message": message,
            "data": data,
        }
    )
