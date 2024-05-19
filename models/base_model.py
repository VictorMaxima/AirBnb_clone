#!/usr/bin/python3
""" contains the class definition for BaseModel"""
import datetime
import models
import uuid

class BaseModel():
    """ Defines the base model class """

    def __init__(self, *args, **kwargs):
        """ defines the initialization process of the base model class"""
        _format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.datetime.strptime(value, _format)
                else:
                    self.__dict__[key] = kwargs[key]
        else: 
            models.storage.new(self)
            


    def __str__(self):
        """ defines the string representation of the base class """       
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ defines the save method for the class BaseModel"""
        self.updated_at = datetime.datetime.today()
        models.storage.save()

    def to_dict(self):
        """ returns a comprehensive dictionary representation of the instance """
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.created_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['id'] = self.id
        return new_dict
