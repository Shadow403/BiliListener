import os
from config import config
from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import scoped_session, sessionmaker

from .model import *


def config_db_engine():
    database_path = f"{config.db_path}/config.db"
    engine = create_engine(f"sqlite:///{database_path}")
    return engine

def config_database_init():
    if not os.path.exists(config.db_path):
        os.makedirs(config.db_path)
    if not os.path.exists(config.json_path):
        os.makedirs(config.json_path)

    engine = config_db_engine()
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


def worker_db_engine(db_name_path):
    engine = create_engine(f"sqlite:///{config.db_path}/{db_name_path}.db")
    return engine

def worker_database_init(db_name_path):
    engine = worker_db_engine(db_name_path)
    SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    data_base.metadata.create_all(engine)

    return SessionLocal

@contextmanager
def get_db_worker_session(uid, uuid):
    if not os.path.exists(f"{config.db_path}/{uid}"):
        os.makedirs(f"{config.db_path}/{uid}")

    SessionLocal = worker_database_init(f"{uid}/{uuid}")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
