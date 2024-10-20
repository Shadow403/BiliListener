import time
from datetime import datetime

async def _nowtime(
        info: bool = False,
        timestamp: bool = False,
        formate: str = "%Y-%m-%d %H:%M:%S"
    ):
    """
    ### info (信息样式)
        - %Y-%m-%d %H:%M:%S UTC+8
    ### timestamp (时间戳)
    ### formate (时间格式)
    """

    if timestamp == True:
        ts = int(time.time())
        return ts

    now = datetime.now()
    formatTime = now.strftime(formate)

    if info == True:
        formatTime += " [UTC+8]"

    return formatTime
