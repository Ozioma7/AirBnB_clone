#!/usr/bin/python3
"""
 Defining the base model class
"""

import uuid
import datetime


class BaseModel:
    """
    class BaseModel that defines all common
    attributes/methods for other classes
    """
    def __init__(self):
        """Initialization"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """String that prints class name, id and class dictionary"""
        class_str = "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
        return class_str

    def save(self):
        """Updates"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
