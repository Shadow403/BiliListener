import json
from config import PathConfig

async def _r_read_cache():
    with open(PathConfig.CACHE_Path, "r") as x:
        cache = json.load(x)
    return cache

async def _r_read_uidlist():
    with open(PathConfig.UIDLIST_Path, "r") as x:
        uids = json.load(x)
    return uids
