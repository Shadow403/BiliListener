import json
from ..base_return import *
from fastapi import APIRouter
from config import WebAPI, PathConfig
from sqlalchemy.orm import sessionmaker
from ..utils import _parmTest, _readFile
from sqlalchemy import create_engine, MetaData

router = APIRouter(prefix=WebAPI.PREFIX)

@router.get("/data/{uid}")
async def _r_shortjson(uid):
    tParm = await _parmTest(uid)
    if tParm != True:
        return tParm
    path, liveData = await _readFile(uid)
    if liveData == False:
        return ret_203(message="uid not found")
    shortData = liveData["data"]
    if "0" in shortData:
        del shortData["0"]
    return ret_200(data=shortData)

@router.get("/data/{uid}/{id}")
async def _r_db2json(uid, id):
    tParm = await _parmTest(uid)
    if tParm != True:
        return tParm
    tParm = await _parmTest(id)
    if tParm != True:
        return tParm
    id = int(id)
    path, liveData = await _readFile(uid)
    if liveData == False:
        return ret_203(message="uid not found")
    liveList = liveData["data"]
    recd_num = len(liveList)
    if id >= recd_num:
        return ret_202(message="id out of range")

    # todo update func
    keys = list(liveList.keys())
    liveSingle = keys[-(id + 1)]
    try:
        if keys[-(recd_num+1-id)] == "0":
            return ret_203(message="top key is invisible")
    except Exception as e:
        pass
    #

    queryData = liveList[liveSingle]
    engine = create_engine(f"sqlite:///{path}/{queryData["stsp"]}.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables["statistics"]
    rows = session.query(table).all()
    data = [row._asdict() for row in rows]
    DBdata = json.loads(json.dumps(data, ensure_ascii=False, indent=4))
    session.close()

    retData = {
        "list_num": recd_num - 1,
        "last_live_tsp": liveData["etsp"],
        "statistics": queryData,
        "query_db": DBdata
    }

    return ret_200(data=retData)
