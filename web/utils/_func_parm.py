from ..base_return import *

async def _parmTest(parm):
    if not parm.isdigit():
        return ret_201(message="parm must be number")
    parm = int(parm)
    if parm < 0:
        return ret_201(message="parm must be positive number")
    return True
