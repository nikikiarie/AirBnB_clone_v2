#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
import sqlalchemy
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table


class Place(BaseModel, Base):
    """Place representation"""
    if models.st_s == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenities = relationship("Review", backref="place")
        reviews = relationship("Amenity", secondary="place_amenity",
                               backref="place_amenities",
                               viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """place initialization"""
        super().__init__(*args, **kwargs)

    if models.st_s != 'db':
        @property
        def reviews(self):
            """return review instance"""
            from models.review import Review
            list_review = []
            reviews_all = models.storage.all(Review)
            for r in reviews_all.values():
                if r.place_id == self.id:
                    list_review.append(r)
            return list_review
        
        @property
        def amenities(self):
            """returns amenities instances"""
            from models.amenity import Amenity
            a_amenities = []
            amenities_list = models.storage.all(Amenity)
            for a in amenities_list.values():
                if a.place_id == self.id:
                    a_amenities.append(a)
            return a_amenities
        