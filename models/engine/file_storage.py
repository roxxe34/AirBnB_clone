#!/usr/bin/python3
"""Define FileStorage class"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """Define FileStorage class
        serilisation/Deserielization
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns dict """
        return type(self).__objects

    def new(self, obj):
        """ Sets new object in dictionary """
        if obj:
            self.__objects["{}.{}".format(
                obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ Serializes __objects = {}"""
        new_json_file = {}
        with open(FileStorage.__file_path, mode="w") as jfile:
            for key, value in self.__objects.items():
                new_json_file[key] = value.to_dict()
                """JSON encoder and decoder"""
            json.dump(new_json_file, jfile)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return