from config import config
from .utils import func_formate_ts

from database.model import *
from database.utils import func_timestamp
from database.connector import get_db_config_session, get_db_worker_session


class data_commit_handle:
    def __init__(self, uid, uuid):
        self.uuid = uuid
        with get_db_worker_session(f"{uid}/{uuid}") as worker_db_session:
            self.db = worker_db_session

    def data_commit(self, x):
        d = self.db.query(LIVE_STATISTICS).filter(LIVE_STATISTICS.uuid == self.uuid).first()
        d.all_gift=x.all_gift
        d.all_enter=x.all_enter
        d.all_guard=x.all_guard
        d.all_danmaku=x.all_danmaku
        d.all_superchat=x.all_superchat
        self.db.commit()

    def data_enter(self, x):
        row = LIVE_LOGS(
            uid=x.uid,
            name=x.uname,
            type=config._et,
            timestamp= x.timestamp
        )
        self.db.add(row)

    def data_danmaku(self, x):
        row = LIVE_LOGS(
            uid=x.uid,
            name=x.uname,
            type=config._dm,
            inner_type=x.dm_type,
            message=x.msg,
            timestamp= func_formate_ts(x.timestamp)
        )
        self.db.add(row)

    def data_gift(self, x):
        row = LIVE_LOGS(
            uid=x.uid,
            name=x.uname,
            type=config._gf,
            gift_id=x.gift_id,
            gift_name=x.gift_name,
            count=x.num,
            coin_type=x.coin_type,
            price=x.total_coin,
            timestamp= x.timestamp
        )
        self.db.add(row)

    def data_guard(self, x):
        row = LIVE_LOGS(
            uid=x.uid,
            name=x.username,
            type=config._gd,
            inner_type=x.guard_level,
            gift_id=x.gift_id,
            gift_name=x.gift_name,
            coin_type="gold",
            price=x.price,
            timestamp= x.start_time
        )
        self.db.add(row)

    def data_superchat(self, x):
        row = LIVE_LOGS(
            uid=x.uid,
            name=x.uname,
            type=config._sc,
            message=x.message,
            coin_type="gold",
            price=int(x.price) * 1000,
            timestamp= x.start_time
        )
        self.db.add(row)

    def data_finish(self):
        with get_db_config_session() as db:
            x = db.query(LIVE_DATA).filter(LIVE_DATA.uuid == self.uuid).first()
            x.is_finished = True
            x.end_timestamp = func_timestamp()
            db.commit()
