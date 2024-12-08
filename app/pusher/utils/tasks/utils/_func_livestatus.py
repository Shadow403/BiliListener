from .api import api_query_live_status

def func_get_live_status(uid_list):
    live_list = []
    ret_json = api_query_live_status(uid_list)
    if ret_json["code"] != 0:
        return live_list

    for x, c in ret_json["data"].items():
        if c["live_status"] == 1:
            live_list.append(c)

    return live_list
