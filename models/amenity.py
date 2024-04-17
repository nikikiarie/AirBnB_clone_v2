#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
