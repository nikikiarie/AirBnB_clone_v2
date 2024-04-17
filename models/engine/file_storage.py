#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""


import json
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            dict_new = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    dict_new[key] = value
            return dict_new
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            item = obj.__class__.__name__ + "." + obj.id
            self.__objects[item] = obj

    def save(self):
        """Saves storage dictionary to file"""
        obj = {}
        for item in self.__objects:
            obj[item] = self.__objects[item].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj, f)

    def reload(self):
        """Loads storage dictionary from file"""

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            with open(self__file_path, 'r') as f:
                obj = json.load(f)
            for item in obj:
                self.__objects[item] = classes[obj[item]["__class__"]](**obj[item])
        except:
            pass

    def delete(self, obj=None):
        """dletes obj from __objects"""
        if obj is not None:
            item = obj.__class__.__name__ + '.' + obj.id
            if item in self.__objects:
                del self.__objects[item]

    def close(self):
        """deserialize Json file"""
        self.reload()
