from .api import QueryLive

async def _get_uid_rid(uid_list):
    liveList = []
    rJson = await QueryLive(uid_list)
    if rJson["code"] != 0:
        return liveList

    for x, value in rJson["data"].items():
        if value["live_status"] == 1:
            uid = value["uid"]
            room_id = value["room_id"]
            live_time = value["live_time"]
            liveList.append([uid, room_id, live_time])
    return liveList
