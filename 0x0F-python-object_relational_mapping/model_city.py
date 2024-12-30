#!/usr/bin/python3
"""Module that contains the City Class definition"""

from model_state import Base
from sqlalchemy import Column, Integer, String, Foreignkey


class City(Base):
    """City class that maps to the city table"""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
