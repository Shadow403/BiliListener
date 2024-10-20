import os
import time
import json
from .model import Base
from config import PathConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def init_data(uid):
    __TSP__ = int(time.time())
    __FOLDER__ = f"{PathConfig.DATA_Path}/{uid}"
    if not os.path.exists(__FOLDER__):
        os.makedirs(__FOLDER__)

        dictConfig = {
            "status": True,
            "stsp": __TSP__,
            "etsp": None,
            "data": {
                "0": {
                    "stsp": None,
                    "etsp": None,
                    "total": {
                        "_et": None,
                        "_dm": None,
                        "_gf": None,
                        "_gd": None,
                        "_sc": None,
                        "_pc": None,
                    }
                }
            }
        }

        with open(f"{__FOLDER__}/config.json", "w") as x:
            json.dump(dictConfig, x, ensure_ascii=False, indent=4)

    engine = create_engine(f"sqlite:///{__FOLDER__}/{str(__TSP__)}.db")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    return session
