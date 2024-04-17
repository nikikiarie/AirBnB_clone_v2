#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""


import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from os import getenv
from models import storage 
import sqlalchemy

t = "%Y-%m-%dT%H:%M:%S.%f"

if models.st_s = "db":
    Base = declarative_base()
else:
    Base = object



class BaseModel:
    """A base class for all hbnb models"""


    if models.st_s =="db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)


    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if  kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], t)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], t)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at


    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictn = self.__dict__.copy()
        if "created_at" in dictn:
            dictn["created_at"] = dictn["created_at"].strftime(t)
        if "updated_at" in dictn:
            dictn["updated_at"] = dictn["updated_at"].strftime(t)
        dictn["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in dictn:
            del dictn["_sa_instance_state"]
        return dictn

    def delete(self):
        """delete instance"""
        storage.delete(self)
