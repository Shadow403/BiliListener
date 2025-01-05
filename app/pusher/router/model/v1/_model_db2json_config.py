from typing import List
from pydantic import BaseModel, Field

class Base(BaseModel):
    uid: int = Field(example=3949941, description="用户ID")
    uuid: str = Field(example="e823f5f1-fdc9-54d8-a39c-9e8aaeffb665", description="唯一标识符")
    name: str = Field(example="阳光男孩小丑熊", description="用户名")
    live_time: int = Field(example=1734087823, description="直播时间")
    live_title: str = Field(example="新版小丑无敌了", description="直播标题")
    live_cover_url: str = Field(example="https://i0.hdslb.com/bfs/live/new_room_cover/3d15c197c36e794d49f8863822b2c67b2b5ebbf1.jpg", description="直播封面URL")
    live_area: int = Field(example=4, description="直播区域")
    live_area_name: str = Field(example="电子竞技", description="直播区域名称")
    live_area_v2_id: int = Field(example=86, description="直播区域V2 ID")
    live_area_v2_name: str = Field(example="英雄联盟", description="直播区域V2名称")
    live_area_v2_parent_id: int = Field(example=2, description="直播区域V2父ID")
    live_area_v2_parent_name: str = Field(example="网游", description="直播区域V2父名称")
    live_tags: str = Field(example="阳光大男孩", description="直播标签")
    live_tags_name: str = Field(example="英雄联盟,DOTA2,星际争霸2,CSGO,风暴英雄", description="直播标签名称")
    if_full: bool = Field(example=False, description="是否全屏")
    is_finished: bool = Field(example=False, description="是否结束")
    start_timestamp: int = Field(example=1734096467, description="开始时间戳")
    end_timestamp: int = Field(example=0, description="结束时间戳")

class LiveConfig(BaseModel):
    uid: int = Field(example=3949941, description="用户ID")
    uuid: str = Field(example="e823f5f1-fdc9-54d8-a39c-9e8aaeffb665", description="唯一标识符")
    name: str = Field(example="阳光男孩小丑熊", description="用户名")
    live_time: int = Field(example=1734087823, description="直播时间")
    live_title: str = Field(example="新版小丑无敌了", description="直播标题")
    live_cover_url: str = Field(example="https://i0.hdslb.com/bfs/live/new_room_cover/3d15c197c36e794d49f8863822b2c67b2b5ebbf1.jpg", description="直播封面URL")
    live_area: int = Field(example=4, description="直播区域")
    live_area_name: str = Field(example="电子竞技", description="直播区域名称")
    live_area_v2_id: int = Field(example=86, description="直播区域V2 ID")
    live_area_v2_name: str = Field(example="英雄联盟", description="直播区域V2名称")
    live_area_v2_parent_id: int = Field(example=2, description="直播区域V2父ID")
    live_area_v2_parent_name: str = Field(example="网游", description="直播区域V2父名称")
    live_tags: str = Field(example="阳光大男孩", description="直播标签")
    live_tags_name: str = Field(example="英雄联盟,DOTA2,星际争霸2,CSGO,风暴英雄", description="直播标签名称")
    if_full: bool = Field(example=False, description="是否全屏")
    is_finished: bool = Field(example=False, description="是否结束")
    start_timestamp: int = Field(example=1734096467, description="开始时间戳")
    end_timestamp: int = Field(example=0, description="结束时间戳")

class Data(BaseModel):
    uid: str = Field(example="3949941", description="用户ID")
    live_count: int = Field(example=1, description="直播数量")
    live_config: List[LiveConfig] = Field(..., description="直播配置")

class get_config_db2json(BaseModel):
    code: int = Field(example=0, description="状态码")
    message: str = Field(example="success", description="状态信息")
    data: Data = Field(..., description="数据")
