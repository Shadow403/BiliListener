from pydantic import BaseModel, Field

class Data(BaseModel):
    server_time: str = Field(example="2024-12-14 00:50:02 [UTC+8]", description="服务器时间")
    server_ntsp: int = Field(example=1734108602, description="服务器NTP时间戳")

class get_api(BaseModel):
    code: int = Field(example=0, description="状态码")
    message: str = Field(example="success", description="状态信息")
    data: Data = Field(..., description="数据")
