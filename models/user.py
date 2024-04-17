#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import models
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import sqlalchemy

class User(BaseModel):
    """This class defines a user by various attributes"""
    if models.storage_t = 'db':
        __tablename__ : 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''


    def __init__(self, *args, **kwargs):
        """Initialize User"""
        super().__init__(*args, kwargs)
