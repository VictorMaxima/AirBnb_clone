#!/usr/bin/python3
""" contains unittests for the File Storage class """

import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
class Test_new(unittest.TestCase):
    """contains teh unittests for the new() method of FileStorage """
    
    def test_new_works(self):
        a = BaseModel()
        models.storage.new(a)
        self.assertIn("BaseModel."+a.id, models.storage.all().keys())

class Test_all(unittest.TestCase):
    """contains the tests for the all() method of fileStorage"""
    def test_all(self):
        a = BaseModel()
        self.assertIn(a, models.storage.all().values())
class Test_save(unittest.TestCase):
    """ contains test for the save method of FileStorage """
    def test_save_works(self):
        a = BaseModel()
        models.storage.save()
        test = ""
        with open("file.json", 'r') as f:
            test = f.read()
        self.assertIn("BaseModel."+a.id, test)
class Test_reload(unittest.TestCase):
    """ contains test for the reload method of FileStorage """
    def test_reload_works(self):
        a = BaseModel()
        models.storage.save()
        models.storage.reload()
        self.assertIn("BaseModel."+a.id, FileStorage._FileStorage__objects)

if __name__ == "__main__":
    unittest.main()
