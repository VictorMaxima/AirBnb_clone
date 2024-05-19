#!/usr/bin/python3
""" initializes file storage for the airbnb clone """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
