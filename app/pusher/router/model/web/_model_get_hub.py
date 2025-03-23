from pydantic import BaseModel, Field

class Total(BaseModel):
    gift: int = Field(example=0, description="礼物数量")
    enter: int = Field(example=0, description="进入房间次数")
    guard: int = Field(example=0, description="守护数量")
    danmaku: int = Field(example=0, description="弹幕数量")
    superchat: int = Field(example=0, description="超级聊天数量")

class Data(BaseModel):
    time: str = Field(example="2025-01-29 01:20:45", description="时间")
    uids: int = Field(example=1, description="用户ID数量")
    uids_listening: int = Field(example=0, description="正在听的用户数量")
    live_count: int = Field(example=0, description="直播数量")
    total: Total

class get_hub(BaseModel):
    code: int = Field(example=0, description="状态码")
    message: str = Field(example="success", description="状态信息")
    data: Data
