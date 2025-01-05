from pydantic import BaseModel, Field

class Total(BaseModel):
    gift: int = Field(example=999, description="礼物数量")
    enter: int = Field(example=999, description="进入房间次数")
    guard: int = Field(example=999, description="舰队数量")
    danmaku: int = Field(example=999, description="弹幕数量")
    superchat: int = Field(example=999, description="超级聊天数量")

class Data(BaseModel):
    count: int = Field(example=999, description="直播记录总数")
    total: Total

class get_total(BaseModel):
    code: int = Field(example=0, description="状态码")
    message: str = Field(example="success", description="状态信息")
    data: Data
 