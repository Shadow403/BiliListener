from .utils import *
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

data_base = declarative_base()
config_base = declarative_base()

class LIVE_LOGS(data_base):
    __tablename__ = "live_logs"
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    type = Column(Integer, nullable=False)
    inner_type = Column(Integer)
    message = Column(String)
    gift_id = Column(Integer)
    gift_name = Column(String)
    coin_type = Column(String)
    price = Column(Integer)
    count = Column(Integer)
    timestamp = Column(Integer, nullable=False)

    def live_logs_json(self):
        json_row = {
            "uid": self.uid,
            "name": self.name,
            "type": self.type,
            "inner_type": self.inner_type,
            "message": self.message,
            "gift_id": self.gift_id,
            "gift_name": self.gift_name,
            "coin_type": self.coin_type,
            "price": self.price,
            "count": self.count,
            "timestamp": self.timestamp
        }

        json_row = {k: v for k, v in json_row.items() if v is not None}

        return json_row

class LIVE_STATISTICS(data_base):
    __tablename__ = "live_statistics"
    id = Column(Integer, primary_key=True)
    uuid = Column(String, nullable=False)

    all_gift = Column(Integer, default=0)        # 1002
    all_enter = Column(Integer, default=0)       # 1000
    all_guard = Column(Integer, default=0)       # 1003
    all_danmaku = Column(Integer, default=0)     # 1001
    all_superchat = Column(Integer, default=0)   # 1004

    def live_statistics_json(self):
        json_row = {
            # "uuid": self.uuid,
            "all_gift": self.all_gift,
            "all_enter": self.all_enter,
            "all_guard": self.all_guard,
            "all_danmaku": self.all_danmaku,
            "all_superchat": self.all_superchat
        }

        return json_row

# ///

class UIDS(config_base):
    __tablename__ = "uids"
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, nullable=False)
    is_ban = Column(Boolean)
    is_live = Column(Boolean)
    add_timestamp = Column(Integer, default=func_timestamp())

    def uids_json(self):
        json_row = {
            "uid": self.uid,
            # "is_ban": self.is_ban,
            "is_live": self.is_live,
            # "add_timestamp": self.add_timestamp
        }

        return json_row

class LIVE_DATA(config_base):
    __tablename__ = "live_data"
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, nullable=False)
    uuid = Column(String, nullable=False)
    name = Column(String, nullable=False)

    live_time = Column(Integer, nullable=False)
    live_title = Column(String)
    live_cover_url = Column(String)
    live_area = Column(Integer)
    live_area_name = Column(String)
    live_area_v2_id = Column(Integer)
    live_area_v2_name = Column(String)
    live_area_v2_parent_id = Column(Integer)
    live_area_v2_parent_name = Column(String)
    live_tags = Column(String)
    live_tags_name = Column(String)

    if_full = Column(Boolean, default=True)
    is_finished = Column(Boolean, default=False)

    all_gift = Column(Integer, default=0)        # 1002
    all_enter = Column(Integer, default=0)       # 1000
    all_guard = Column(Integer, default=0)       # 1003
    all_danmaku = Column(Integer, default=0)     # 1001
    all_superchat = Column(Integer, default=0)   # 1004

    start_timestamp = Column(Integer, default=func_timestamp())
    end_timestamp = Column(Integer, default=0)

    def live_data_json(self):
        json_row = {
            "uid": self.uid,
            "uuid": self.uuid,
            "name": self.name,

            "live_time": self.live_time,
            "live_title": self.live_title,
            "live_cover_url": self.live_cover_url,
            "live_area": self.live_area,
            "live_area_name": self.live_area_name,
            "live_area_v2_id": self.live_area_v2_id,
            "live_area_v2_name": self.live_area_v2_name,
            "live_area_v2_parent_id": self.live_area_v2_parent_id,
            "live_area_v2_parent_name": self.live_area_v2_parent_name,
            "live_tags": self.live_tags,
            "live_tags_name": self.live_tags_name,

            "if_full": self.if_full,
            "is_finished": self.is_finished,

            "all_gift": self.all_gift,
            "all_enter": self.all_enter,
            "all_guard": self.all_guard,
            "all_danmaku": self.all_danmaku,
            "all_superchat": self.all_superchat,

            "start_timestamp": self.start_timestamp,
            "end_timestamp": self.end_timestamp
        }

        return json_row
