from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class _init_(Base):
    __tablename__ = "statistics"
    id = Column(Integer, primary_key=True)
    type = Column(Integer, nullable=False)
    coin_type = Column(String)
    name = Column(String, nullable=False)
    uid = Column(Integer, nullable=False)
    message = Column(String)
    gift_id = Column(Integer)
    gift_name = Column(String)
    price = Column(Integer)
    count = Column(Integer)
    tsp = Column(Integer, nullable=False)
