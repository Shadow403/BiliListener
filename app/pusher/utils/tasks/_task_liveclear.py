from blivedm import logger

from .utils import func_get_live_status

from database.model import UIDS
from database.connector import get_db_config_session


def live_clear_inspectors():
    with get_db_config_session() as config_db_session:
        uid_query_list = config_db_session.query(UIDS.uid).filter(UIDS.is_live == True).all()
        uid_list = [uid[0] for uid in uid_query_list]
        uid_dict = {"uids": uid_list}
        live_config = func_get_live_status(uid_dict, False)

        for x in live_config:
            uid = x["uid"]
            live_status_update = config_db_session.query(UIDS).filter(UIDS.uid == uid).first()
            live_status_update.is_live = False

            config_db_session.commit()
            logger.info(f"PREPARING LISTENING {uid}")
