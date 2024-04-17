#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import sqlalchemy
import models
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity Class"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
