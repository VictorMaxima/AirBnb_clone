#!/bin/bash/python3
""" contains the definition of the state class """
from models.base_model import BaseModel


class State(BaseModel):
    """ class of the State model
    Attributes:
        name: name of the state
    """
    name = ""
