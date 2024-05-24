#!/usr/bin/python3
"""contains the unittest for the city model """
import unittest
from models.city import City
from datetime import datetime
from time import sleep


class TestInstantiation(unittest.TestCase):
    """ Contains tests for the instantiation of the City class"""

    def test_correct_type_of_attributes(self):
        self.assertEqual(str, type(City().id))
        self.assertEqual(datetime, type(City().created_at))
        self.assertEqual(datetime, type(City().updated_at))
        
    def test_dates_not_equal_for_two_objects(self):
        a = City()
        sleep(0.05)
        b = City()
        self.assertNotEqual(a.created_at, b.created_at)
        self.assertNotEqual(a.updated_at, b.updated_at)
    
    def test_create_from_dict(self):
        a = City()
        a_dict = a.to_dict()
        b = City(**a_dict)
        self.assertEqual(b.id, a.id)
        self.assertEqual(a.created_at, b.created_at)
        self.assertEqual(a.updated_at, b.updated_at)
