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
