from typing import List
from pydantic import BaseModel, Field

class Data(BaseModel):
    uid: List[int] = Field(example=[3949941], description="用户ID列表")

class get_uids(BaseModel):
    code: int = Field(example=0, description="状态码")
    message: str = Field(example="success", description="状态信息")
    data: Data = Field(..., description="数据")
