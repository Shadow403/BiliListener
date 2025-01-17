from typing import Optional
from pydantic import BaseModel, Field

class WatchedShow(BaseModel):
    switch: bool = Field(example=True, description="观看显示开关")
    num: int = Field(example=31246, description="观看人数")
    text_small: str = Field(example="3.1万", description="小文本显示")
    text_large: str = Field(example="3.1万人看过", description="大文本显示")
    icon: str = Field(example="https://i0.hdslb.com/bfs/live/a725a9e61242ef44d764ac911691a7ce07f36c1d.png", description="图标链接")
    icon_location: Optional[str] = Field(None, description="图标位置")
    icon_web: str = Field(example="https://i0.hdslb.com/bfs/live/8d9d0f33ef8bf6f308742752d13dd0df731df19c.png", description="网页图标链接")

class LiveRoom(BaseModel):
    roomStatus: int = Field(example=1, description="房间状态")
    liveStatus: int = Field(example=1, description="直播状态")
    url: str = Field(example="https://live.bilibili.com/22907643?broadcast_type=0&is_room_feed=1", description="直播房间链接")
    title: str = Field(example="熊：偷野流冲宗师！", description="直播标题")
    cover: str = Field(example="https://i0.hdslb.com/bfs/live/new_room_cover/3d15c197c36e794d49f8863822b2c67b2b5ebbf1.jpg", description="直播封面")
    roomid: int = Field(example=22907643, description="房间ID")
    roundStatus: int = Field(example=0, description="轮播状态")
    broadcast_type: int = Field(example=0, description="广播类型")
    watched_show: WatchedShow = Field(..., description="观看信息")

class Data(BaseModel):
    ststus: bool = Field(example=True, description="状态")
    uid: int = Field(example=3949941, description="用户ID")
    uname: str = Field(example="阳光男孩小丑熊", description="用户名")
    live_room: LiveRoom = Field(..., description="直播房间信息")

class put_add_uid(BaseModel):
    code: int = Field(example=0, description="状态码")
    message: str = Field(example="added", description="状态信息")
    data: Data = Field(..., description="数据")
