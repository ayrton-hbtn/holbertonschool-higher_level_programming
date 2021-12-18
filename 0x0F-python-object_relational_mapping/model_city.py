#!/usr/bin/python3
""" contains the class definition of a City """


from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base, State


class City(Base):
    """ class city """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id))
