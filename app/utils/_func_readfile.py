import json
from config import PathConfig

async def _r_read_cache():
    config_path = PathConfig.CACHE_Path
    with open(config_path, "r") as x:
        cache = json.load(x)
    return config_path, cache

async def _r_read_uidlist():
    config_path = PathConfig.UIDLIST_Path
    with open(config_path, "r") as x:
        uids = json.load(x)
    return config_path, uids

def _r_read_livedata(uid):
    congfig_path = f"{PathConfig.DATA_Path}/{uid}/config.json"
    with open(congfig_path, "r") as x:
        data = json.load(x)
    return congfig_path, data
