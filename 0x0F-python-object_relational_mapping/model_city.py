#!/usr/bin/python3
"""
Class City
"""
from model_state import Base, State
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Resentation City"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
