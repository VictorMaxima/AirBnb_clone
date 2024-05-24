#!/bin/bash/python3
""" contains the definition of the amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ class of the user model
    Attributes:
        name(str): name of the amenity
    """
    name = ""
