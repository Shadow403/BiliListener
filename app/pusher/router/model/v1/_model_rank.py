from typing import List
from pydantic import BaseModel, Field

class AllGift(BaseModel):
    all: int = Field(example=473, description="总礼物数量")
    gold: int = Field(example=400, description="黄金礼物数量")
    silver: int = Field(example=73, description="白银礼物数量")

class LiveConfig(BaseModel):
    uid: int = Field(example=14270000, description="用户ID")
    uuid: str = Field(example="c8f379eb-8a17-583b-b866-aed30db587e8", description="UUID")
    name: str = Field(example="Yom****", description="用户名")
    live_time: int = Field(example=1735876537, description="直播时间")
    live_title: str = Field(example="这是彩六第一女杀手，你敢和她对视吗？", description="直播标题")
    live_cover_url: str = Field(example="https://i0.hdslb.com/bfs/live/new_room_cover/bb32942d31f8ab8123b8bf443e66aa27b9b08281.jpg", description="直播封面URL")
    live_area: int = Field(example=3, description="直播区域")
    live_area_name: str = Field(example="网络游戏", description="直播区域名称")
    live_area_v2_id: int = Field(example=601, description="直播区域V2 ID")
    live_area_v2_name: str = Field(example="综合射击", description="直播区域V2名称")
    live_area_v2_parent_id: int = Field(example=2, description="直播区域V2父ID")
    live_area_v2_parent_name: str = Field(example="网游", description="直播区域V2父名称")
    live_tags: str = Field(example="APEX,斗地主,主机游戏,单机游戏,PS5,NS,索尼,FPS,萌妹,无畏契约,三角洲,彩虹六号", description="直播标签")
    live_tags_name: str = Field(example="守望先锋,炉石传说,剑网3,dnf,最终幻想14,坦克世界", description="直播标签名称")
    if_full: bool = Field(example=True, description="是否全屏")
    is_finished: bool = Field(example=True, description="是否结束")
    all_gift: AllGift
    all_price: int = Field(example=342312, description="总价格")
    all_enter: int = Field(example=54603, description="进入次数")
    all_guard: int = Field(example=3, description="守护数量")
    all_danmaku: int = Field(example=10367, description="弹幕数量")
    all_superchat: int = Field(example=4, description="超级聊天数量")
    start_timestamp: int = Field(example=1735652452, description="开始时间戳")
    end_timestamp: int = Field(example=1735926660, description="结束时间戳")

class Data(BaseModel):
    count: int = Field(example=1, description="计数")
    live_config_list: List[LiveConfig] = Field(description="直播配置列表")

class get_rank(BaseModel):
    code: int = Field(example=0, description="状态码")
    message: str = Field(example="success", description="状态信息")
    data: Data
