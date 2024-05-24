#!/bin/bash/python3
""" contains the definition of the place class """
from models.base_model import BaseModel


class Place(BaseModel):
    """ class of the place model
    Attributes:
        city_id(str): id of the city
        user_id(str): id of the user
        name: name of place
        description: description
        number_rooms(int): number of rooms
        number_bathrooms(int): number of bathrooms
        max_guest(int): maximum number of guests
        price_by_night(int): price per night
        latitude(float): latitude
        longitude(float): longitude
        amenity_ids(list): list of amenity id's
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
