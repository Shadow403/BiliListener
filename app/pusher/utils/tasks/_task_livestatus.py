import subprocess
from blivedm import logger

from .utils import func_get_live_status
from database.model import UIDS, LIVE_DATA
from database.utils import func_generate_uuid
from config import config, __version__, __platform__
from database.connector import get_db_config_session


def live_status_inspectors():
    with get_db_config_session() as config_db_session:
        uid_query_list = config_db_session.query(UIDS.uid).filter(UIDS.is_live == False, UIDS.is_ban == False).all()
        uid_list = [uid[0] for uid in uid_query_list]
        uid_dict = {"uids": uid_list}
        live_config = func_get_live_status(uid_dict)

        for x in live_config:
            uid = x["uid"]
            rid = x["room_id"]
            live_time = x["live_time"]
            uuid = func_generate_uuid(uid, live_time)
            new_live = LIVE_DATA(
                uid = uid,
                uuid = uuid,
                name = x["uname"],
                live_time = live_time,
                live_title = x["title"],
                live_cover_url = x["cover_from_user"],
                live_area = x["area"],
                live_area_name = x["area_name"],
                live_area_v2_id = x["area_v2_id"],
                live_area_v2_name = x["area_v2_name"],
                live_area_v2_parent_id = x["area_v2_parent_id"],
                live_area_v2_parent_name = x["area_v2_parent_name"],
                live_tags = x["tags"],
                live_tags_name = x["tag_name"]
            )

            live_status_update = config_db_session.query(UIDS).filter(UIDS.uid == uid).first()
            live_status_update.is_live = True

            config_db_session.add(new_live)
            config_db_session.commit()

            command = f"worker-{__platform__}-{__version__}.exe {uid} {rid} {live_time}"

            if config.hide_console:
                subprocess.Popen(["cmd", "/c", command], creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                subprocess.Popen(["cmd", "/c", command], creationflags=subprocess.CREATE_NEW_CONSOLE)

            logger.warning(f"STARTING LISTENING {uid}")
