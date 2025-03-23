import time
import multiprocessing
from blivedm import logger

from config import config
from database.model import UIDS
from .utils import func_get_live_status
from ...worker.app import worker_initializer
from database.connector import get_db_config_session


def live_status_loop():
    logger.success("START LIVE STATUS LOOP")
    while True:
        try:
            live_status_inspectors()
            time.sleep(config.push_query_delay)
        except KeyboardInterrupt:
            logger.success("STOP LIVE STATUS LOOP")
            break

def live_status_inspectors():
    logger.info("QUERY LIVE STATUS")
    with get_db_config_session() as config_db_session:
        uid_query_list = config_db_session.query(UIDS.uid).filter(UIDS.is_live == False, UIDS.is_ban == False).all()

    uid_list = [uid[0] for uid in uid_query_list]
    uid_dict = {"uids": uid_list}
    live_config = func_get_live_status(uid_dict)

    for x in live_config:
        if config.debug:
            logger.debug(x)

        with get_db_config_session() as config_db_session:
            config_db_session.query(UIDS).filter(UIDS.uid == x["uid"]).update({UIDS.is_live: True})
            config_db_session.commit()

        process = multiprocessing.Process(target=worker_initializer, args=(x, ))
        process.start()

        logger.warning(f"STARTING LISTENING {x['uid']}")
