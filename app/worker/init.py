import os

from config import PathConfig

from database.utils import func_generate_uuid
from database.model import LIVE_STATISTICS, LIVE_DATA
from database.connector import get_db_worker_session, get_db_config_session


def worker_db_initializer(live_uid, live_timestamp):
    uuid = f"{live_uid}000{live_timestamp}"
    uuid_str = func_generate_uuid(uuid)

    if not os.path.exists(f"{PathConfig.DATA_Path}/{live_uid}"):
        os.makedirs(f"{PathConfig.DATA_Path}/{live_uid}")

    db_name_path = f"{live_uid}/{uuid_str}"
    with get_db_worker_session(db_name_path) as worker_db_session:
        live_statistics = worker_db_session.query(
            LIVE_STATISTICS).filter(LIVE_STATISTICS.uuid == uuid_str).first()

        if live_statistics == None:
            new_live = LIVE_STATISTICS(
                uuid=uuid_str,
            )
            worker_db_session.add(new_live)
            worker_db_session.commit()

        else:
            with get_db_config_session() as config_db_session:
                live_data = config_db_session.query(
                    LIVE_DATA).filter(LIVE_DATA.uuid == uuid_str).first()
                if live_data:
                    live_data.if_full = False
                    config_db_session.commit()

        live_statistics_lasted = worker_db_session.query(
            LIVE_STATISTICS).filter(LIVE_STATISTICS.uuid == uuid_str).first()

    return live_statistics_lasted, uuid_str
