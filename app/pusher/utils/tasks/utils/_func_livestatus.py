from blivedm import logger

from .api import api_query_live_status

def func_get_live_status(
    uid_list: list = [],
    check_live_code: bool = True,
):
    live_list = []
    if check_live_code:
        live_status = 1
    else:
        live_status = 0

    ret_json = api_query_live_status(uid_list)
    if ret_json["code"] != 0:
        return live_list

    try:
        for x, c in ret_json["data"].items():
            if c["live_status"] == live_status:
                live_list.append(c)
    except:
        # logger.error("UID错误 {}")
        return []

    return live_list
