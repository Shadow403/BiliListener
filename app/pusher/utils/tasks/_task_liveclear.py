import time
from blivedm import logger

from config import config
from .utils import func_get_live_status

from database.model import UIDS
from database.connector import get_db_config_session


def live_clear_loop():
    logger.success("START LIVE CLEAR LOOP")
    while True:
        try:
            live_clear_inspectors()
            time.sleep(config.live_clear_delay)
        except KeyboardInterrupt:
            logger.success("STOP LIVE CLEAR LOOP")
            break

def live_status_initializer():
    # logger.info("CLEAR LIVE STATUS")
    with get_db_config_session() as config_db_session:
        config_db_session.query(UIDS).update({UIDS.is_live: False})
        config_db_session.commit()

def live_clear_inspectors():
    logger.info("CLEAR LIVE STATUS")
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
