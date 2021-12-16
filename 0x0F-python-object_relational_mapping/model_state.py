#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.elements import Null
engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], arv[2], argv[3]), pool_pre_ping=True)
session = Session(engine)
Base = declarative_base()
class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128)) != Null