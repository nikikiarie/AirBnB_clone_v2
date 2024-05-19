#!/usr/bin/python3
""" State Module for HBNB project """
import models
import sqlalchemy
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State representation"""
    if models.st_s == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initialize state"""
        super().__init__(*args, **kwargs)

    if models.st_s != "db":
        @property
        def cities(self):
            """list of cities related to state"""
            state_cities = []
            cities_all = models.storage.all(City)
            for city in cities_all.values():
                if city.state_id == self.id:
                    state_cities.append(city)
            return state_cities
