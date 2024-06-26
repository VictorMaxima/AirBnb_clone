#!/usr/bin/python3
"""contains the unittest for the Review model """
import unittest
from models.review import Review
from datetime import datetime
from time import sleep


class TestInstantiation(unittest.TestCase):
    """ Contains tests for the instantiation of the Review class"""

    def test_correct_type_of_attributes(self):
        self.assertEqual(str, type(Review().id))
        self.assertEqual(datetime, type(Review().created_at))
        self.assertEqual(datetime, type(Review().updated_at))
        
    def test_dates_not_equal_for_two_objects(self):
        a = Review()
        sleep(0.05)
        b = Review()
        self.assertNotEqual(a.created_at, b.created_at)
        self.assertNotEqual(a.updated_at, b.updated_at)
    
    def test_create_from_dict(self):
        a = Review()
        a_dict = a.to_dict()
        b = Review(**a_dict)
        self.assertEqual(b.id, a.id)
        self.assertEqual(a.created_at, b.created_at)
