#!/usr/bin/python3
"""This module defines a class City"""
from models.base_model import BaseModel, Base
import models
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import sqlalchemy

class User(BaseModel):
    """This class defines a user by various attributes"""
    if models.st_s = 'db':
        __tablename__ : 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ''
        name = ''


    def __init__(self, *args, **kwargs):
        """Initialize User"""
        super().__init__(*args, kwargs)
