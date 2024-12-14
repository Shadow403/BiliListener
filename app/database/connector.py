import os
from config import config
from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import scoped_session, sessionmaker

from .model import *


def config_database_init():
    if not os.path.exists(config.data_path):
        os.makedirs(config.data_path)

    database_path = f"{config.data_path}/config.db"
    engine = create_engine(f"sqlite:///{database_path}")
    SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    config_base.metadata.create_all(engine)

    return SessionLocal

@contextmanager
def get_db_config_session():
    SessionLocal = config_database_init()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def worker_database_init(db_name_path):
    engine = create_engine(f"sqlite:///{config.data_path}/{db_name_path}.db")
    SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    data_base.metadata.create_all(engine)

    return SessionLocal

@contextmanager
def get_db_worker_session(db_name_path):
    SessionLocal = worker_database_init(db_name_path)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
