import json
import time
from sqlalchemy import func
from colorama import Fore, Style

from config import config
from database.model import *
from ...utils._func_time import func_time
from ...base_return import ret_200_concatenation
from database.connector import get_db_config_session


def ws_hub(websocket):
    try:
        while True:
            print(f"{Fore.GREEN}INFO{Style.RESET_ALL}:     WEBSOCKET PUSHING")
            with get_db_config_session() as session:
                uids_count = len(session.query(UIDS.uid).all())
                live_count = len(session.query(LIVE_DATA).all())
                uids_listening_count = len(session.query(UIDS.uid).filter(UIDS.is_live == True).all())

                gf, et, gd, dm, sc = session.query(
                    func.sum(LIVE_DATA.all_gift).label('total_gift'),
                    func.sum(LIVE_DATA.all_enter).label('total_enter'),
                    func.sum(LIVE_DATA.all_guard).label('total_guard'),
                    func.sum(LIVE_DATA.all_danmaku).label('total_danmaku'),
                    func.sum(LIVE_DATA.all_superchat).label('total_superchat')
                ).first()

            total_data = {
                "gift": gf,
                "enter": et,
                "guard": gd,
                "danmaku": dm,
                "superchat": sc
            }

            total_data = {
                k: (v if v is not None else 0) for k, 
                v in total_data.items()}

            full_data = ret_200_concatenation({
                "time": func_time(),
                "uids": uids_count,
                "uids_listening": uids_listening_count,
                "live_count": live_count,
                "total": total_data
            })

            json_data = json.dumps(full_data)

            websocket.send(json_data)
            time.sleep(config.ws_push_delay)
    except Exception as e:
        if config.debug:
            print(f"{Fore.YELLOW}WARNING{Style.RESET_ALL}:    WebSocket: {e}")
