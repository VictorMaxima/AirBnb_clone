#!/usr/bin/python3
"""contains the unittest for the user model """
import unittest
from models.user import User
from datetime import datetime
from time import sleep


class TestInstantiation(unittest.TestCase):
    """ Contains tests for the instantiation of the user class"""

    def test_correct_type_of_attributes(self):
        self.assertEqual(str, type(User().id))
        self.assertEqual(datetime, type(User().created_at))
        self.assertEqual(datetime, type(User().updated_at))
        
    def test_dates_not_equal_for_two_objects(self):
        a = User()
        sleep(0.05)
        b = User()
        self.assertNotEqual(a.created_at, b.created_at)
        self.assertNotEqual(a.updated_at, b.updated_at)
    
    def test_create_from_dict(self):
        a = User()
        a_dict = a.to_dict()
        b = User(**a_dict)
        self.assertEqual(b.id, a.id)
        self.assertEqual(a.created_at, b.created_at)
