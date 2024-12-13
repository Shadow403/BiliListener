from pydantic import BaseModel, Field

class Data(BaseModel):
    pass

class put_add_uid(BaseModel):
    code: int = Field(example=0, description="状态码")
    message: str = Field(example="added", description="状态信息")
    data: Data = Field(..., description="数据")
