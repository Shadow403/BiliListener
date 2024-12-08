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

class LIVE_STATISTICS(data_base):
    __tablename__ = "live_statistics"
    id = Column(Integer, primary_key=True)
    uuid = Column(String, nullable=False)

    all_gift = Column(Integer, default=0)        # 1002
    all_enter = Column(Integer, default=0)       # 1000
    all_guard = Column(Integer, default=0)       # 1003
    all_danmaku = Column(Integer, default=0)     # 1001
    all_superchat = Column(Integer, default=0)   # 1004

# ///

class UIDS(config_base):
    __tablename__ = "uids"
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, nullable=False)
    is_ban = Column(Boolean)
    is_live = Column(Boolean)
    add_timestamp = Column(Integer, default=func_timestamp())

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

    start_timestamp = Column(Integer, default=func_timestamp())
    end_timestamp = Column(Integer, default=0)
