#!/usr/bin/python3
""" handles the file storage of the airbnb console """
import json
from models.base_model import BaseModel

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
        object_dictionary = { obj_key: obj.to_dict() for obj_key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(object_dictionary, file)
    
    def reload(self):
        """ deserializes the json """
        try: 
            with open(FileStorage.__file_path,'r') as f:
                objects = json.load(f)
                for key, object_rep in objects.items():
                    _class = objects['__class__']
                    del objects['__class__']
                    new = eval((_class)(**object_rep))
                    self.new(eval)
        except: 
            return


