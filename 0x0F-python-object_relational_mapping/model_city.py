#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base, State
import sys

argv = sys.argv
engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                        argv[1], argv[2], argv[3]), pool_pre_ping=True)


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id))
