#!/usr/bin/python3
"""class dbstorage"""


import models
import sqlalchemy
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.base_model import BaseModel, Base
from models.user import User


classes ={"Amenity": Amenity, "City": City, "User": User, "Place": Place, "Review": Review, "State": State}


class DBStorage:
    """rship sql database"""
    __engine = None
    __session = None


    def __init__(self):
        """instatiate dbstorage"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB))

        if HBNB_ENV == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """query db"""
        dict_new = {}
        for cl in classes:
            if cls is None or cls is cl or cls is classes[cl]:
                obj = self.__session.query(classes[cl]).all()
                for ob in obj:
                    item = ob.__class__.__name__ + '.' + ob.id
                    dict_new[item] = ob
        return (dict_new)

    def new(self, obj):
        """add to database"""
        self.__session.add(obj)

    def save(self):
        """save changes to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from db"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads datafrom db"""
        Base.metadata.create_all(self.__engine)
        ft = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ft)
        self.__session = Session

    def close(self):
        """call remove methid"""
        self.__session.remove()
