#!/usr/bin/python3
"""Defines City class inherits that from Base
"""
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship


class City(Base):
    """City class with id and name attributes of each state"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
    # state = relationship("State", back_populates="cities")
