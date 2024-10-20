import json
from config import PathConfig

async def _readFile(parm):
    try:
        __DATA_PARH__ = f"{PathConfig.DATA_Path}/{parm}"
        with open(f"{__DATA_PARH__}/config.json") as x:
            liveData = json.load(x)
    except Exception as e:
        return None, False
    return __DATA_PARH__, liveData

async def _read_uidlist():
    with open(PathConfig.UIDLIST_Path, "r") as x:
        data = json.load(x)
    return data
