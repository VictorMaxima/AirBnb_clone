#!/bin/bash/python3
""" contains the definition of the city class """
from models.base_model import BaseModel


class City(BaseModel):
    """ class of the city model
    Attributes:
        state_id(str): id of the parent state
        name: name of the city
    """
    state_id = ""
    name = ""
