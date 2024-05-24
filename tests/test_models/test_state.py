#!/usr/bin/python3
"""contains the unittest for the state model """
import unittest
from models.state import State
from datetime import datetime
from time import sleep


class TestInstantiation(unittest.TestCase):
    """ Contains tests for the instantiation of the State class"""

    def test_correct_type_of_attributes(self):
        self.assertEqual(str, type(State().id))
        self.assertEqual(datetime, type(State().created_at))
        self.assertEqual(datetime, type(State().updated_at))
        
    def test_dates_not_equal_for_two_objects(self):
        a = State()
        sleep(0.05)
        b = State()
        self.assertNotEqual(a.created_at, b.created_at)
        self.assertNotEqual(a.updated_at, b.updated_at)
    
    def test_create_from_dict(self):
        a = State()
        a_dict = a.to_dict()
        b = State(**a_dict)
        self.assertEqual(b.id, a.id)
        self.assertEqual(a.created_at, b.created_at)
        self.assertEqual(a.updated_at, b.updated_at)
