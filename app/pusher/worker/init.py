from database.model import LIVE_DATA
from database.utils import func_generate_uuid
from database.connector import get_db_config_session


def worker_db_initializer(live_config):
    uid = live_config["uid"]
    rid = live_config["room_id"]
    live_timestamp = live_config["live_time"]
    uuid = func_generate_uuid(uid, live_timestamp)

    with get_db_config_session() as cdb_session:
        live_statistics = cdb_session.query(
            LIVE_DATA).filter(LIVE_DATA.uuid == uuid).first()

        if live_statistics == None:
            live_time = live_config["live_time"]
            new_live = LIVE_DATA(
                uid = uid,
                uuid = uuid,
                name = live_config["uname"],
                live_time = live_time,
                live_title = live_config["title"],
                live_cover_url = live_config["cover_from_user"],
                live_area = live_config["area"],
                live_area_name = live_config["area_name"],
                live_area_v2_id = live_config["area_v2_id"],
                live_area_v2_name = live_config["area_v2_name"],
                live_area_v2_parent_id = live_config["area_v2_parent_id"],
                live_area_v2_parent_name = live_config["area_v2_parent_name"],
                live_tags = live_config["tags"],
                live_tags_name = live_config["tag_name"]
            )
            cdb_session.add(new_live)
            cdb_session.commit()

        else:
            with get_db_config_session() as config_db_session:
                live_data = config_db_session.query(
                    LIVE_DATA).filter(LIVE_DATA.uuid == uuid).first()
                if live_data:
                    live_data.if_full = False
                    config_db_session.commit()

        revert_data = cdb_session.query(
            LIVE_DATA).filter(LIVE_DATA.uuid == uuid).first()

    class ret_class:
        def __init__(self, uid, rid, uuid, revert_data):
            self.uid = uid
            self.rid = rid
            self.uuid = uuid
            self.revert_data = revert_data

    ret_data = ret_class(uid, rid, uuid, revert_data)

    return ret_data
