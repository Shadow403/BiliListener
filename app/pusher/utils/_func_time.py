import time
from datetime import datetime


def func_time(
        info: bool = False,
        timestamp: bool = False,
        formate: str = "%Y-%m-%d %H:%M:%S"
    ):
    if timestamp:
        ts = int(time.time())
        return ts

    now = datetime.now()
    ft = now.strftime(formate)

    if info:
        ft += " [UTC+8]"

    return ft
