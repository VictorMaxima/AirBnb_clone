#!/usr/bin/python3
""" handles the file storage of the airbnb console """
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State


class FileStorage():
    """ the general class for file storage
    Attributes:
    __file_path: file path to the storage file
    __objects: dictionary of objects
     """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        "returns everything in objects"
        return FileStorage.__objects

    def new(self, obj):
        """ adds obj to __objects """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ saves the objects through serialization """
        b = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(b, file)

    def reload(self):
        """ deserializes the json """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objects = json.load(f)
                for key, object_rep in objects.items():
                    _class = object_rep['__class__']
                    del object_rep['__class__']
                    new = eval(_class)(**object_rep)
                    self.new(new)
        except FileNotFoundError:
            return
