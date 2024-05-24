#!/bin/bash/python3
""" contains the definition of the review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ class of the State model
    Attributes:
        place_id: id of the place
        user_id: id of the user
        text: review
    """
    place_id = ""
    user_id = ""
    text = ""
