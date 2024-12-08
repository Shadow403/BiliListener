from .model import *
from config import PathConfig
from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import scoped_session, sessionmaker


def config_database_init():
    database_path = f"{PathConfig.DATA_Path}/config.db"
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
    engine = create_engine(f"sqlite:///{PathConfig.DATA_Path}/{db_name_path}.db")
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
