#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import sqlalchemy
import models
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity Class"""
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""


    def __init__(self, *args, **kwargs):
        """Initialize Amenities"""
        super.__init__(*args, **kwargs)

