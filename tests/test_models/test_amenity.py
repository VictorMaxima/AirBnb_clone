#!/usr/bin/python3
"""contains the unittest for the Amenity model """
import unittest
from models.amenity import Amenity
from datetime import datetime
from time import sleep


class TestInstantiation(unittest.TestCase):
    """ Contains tests for the instantiation of the Amenity class"""

    def test_correct_type_of_attributes(self):
        self.assertEqual(str, type(Amenity().id))
        self.assertEqual(datetime, type(Amenity().created_at))
        self.assertEqual(datetime, type(Amenity().updated_at))
        
    def test_dates_not_equal_for_two_objects(self):
        a = Amenity()
        sleep(0.05)
        b = Amenity()
        self.assertNotEqual(a.created_at, b.created_at)
        self.assertNotEqual(a.updated_at, b.updated_at)
    
    def test_create_from_dict(self):
        a = Amenity()
        a_dict = a.to_dict()
        b = Amenity(**a_dict)
        self.assertEqual(b.id, a.id)
        self.assertEqual(a.created_at, b.created_at)
