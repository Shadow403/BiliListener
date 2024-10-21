import os
import json
from .model import Base
from config import PathConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def init_data(uid, livetime):
    __FOLDER__ = f"{PathConfig.DATA_Path}/{uid}"
    if not os.path.exists(__FOLDER__):
        os.makedirs(__FOLDER__)

        dictConfig = {
            "status": True,
            "stsp": livetime,
            "etsp": None,
            "data": {
                "0": {
                    "stsp": None,
                    "etsp": None,
                    "lost": False,
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

    database_path = f"{__FOLDER__}/{str(livetime)}.db"
    if os.path.exists(database_path):
        lost = True
    else:
        lost = False
    engine = create_engine(f"sqlite:///{database_path}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    return lost, session
