import subprocess
from blivedm import logger

from database.model import UIDS
from config.utils import b64_encode
from .utils import func_get_live_status
from database.connector import get_db_config_session
from config import config, __version__, __platform__, get_type


ex = get_type()

def live_status_inspectors():
    with get_db_config_session() as config_db_session:
        uid_query_list = config_db_session.query(UIDS.uid).filter(UIDS.is_live == False, UIDS.is_ban == False).all()
        uid_list = [uid[0] for uid in uid_query_list]
        uid_dict = {"uids": uid_list}
        live_config = func_get_live_status(uid_dict)

        for x in live_config:
            live_config = b64_encode(str(x))
            command = f"worker-{__platform__}-{__version__}-{ex}.exe {live_config}"
            full_cmd = ["cmd", "/c", command]

            if config.debug:
                print(full_cmd)

            if config.hide_console:
                subprocess.Popen(full_cmd, creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                subprocess.Popen(full_cmd, creationflags=subprocess.CREATE_NEW_CONSOLE)

            logger.warning(f"STARTING LISTENING {x['uid']}")
