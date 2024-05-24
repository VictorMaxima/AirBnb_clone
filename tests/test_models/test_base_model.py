#!/usr/bin/python3
""" Contains the unittests for basemodel class"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestInstantiation(unittest.TestCase):
    """ Contains tests for the instantiation of the base model class"""

    def test_correct_type_of_attributes(self):
        self.assertEqual(str, type(BaseModel().id))
        self.assertEqual(datetime, type(BaseModel().created_at))
        self.assertEqual(datetime, type(BaseModel().updated_at))
        
    def test_dates_not_equal_for_two_objects(self):
        a = BaseModel()
        sleep(0.05)
        b = BaseModel()
        self.assertNotEqual(a.created_at, b.created_at)
        self.assertNotEqual(a.updated_at, b.updated_at)
    
    def test_create_from_dict(self):
        a = BaseModel()
        a_dict = a.to_dict()
        b = BaseModel(**a_dict)
        self.assertEqual(b.id, a.id)
        self.assertEqual(a.created_at, b.created_at)
        

class TestSave(unittest.TestCase):
    """ contains tests for the save method of BaseModel"""
    def test_change_in_updated_at(self):
        a = BaseModel()
        b = a.updated_at
        sleep(0.05)
        a.save()
        self.assertLess(b, a.updated_at)

class Test_To_dict(unittest.TestCase):
    """ contains test for the to_dict method of the BaseModel class """
    def test_dict_contains_keys(self):
        a = BaseModel()
        newdict = a.to_dict()
        self.assertEqual(a.id, newdict['id'])
        self.assertEqual(a.created_at.isoformat(), newdict['created_at'])
        self.assertEqual(type(a.updated_at.isoformat()), type(newdict['updated_at']))
        self.assertEqual(a.__class__.__name__, newdict['__class__'])

if __name__ == "__main__":
    unittest.main()    
