#!/usr/bin/python3
"""
    Testing the BaseModel
"""
import unittest
from models import BaseModel

class TestBaseModel(unittest.TestCase):
    """Testing the class"""

    def test_init(self):
        """Testing Initialization"""
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)

    def test_save(self):
        """Testing Save"""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)

    def test_to_dict(self):
        """Testing to_dict"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_str(self):
        """Testing String"""
        obj = BaseModel()
        obj_str = str(obj)
        self.assertIsInstance(obj_str, str)
        self.assertIn(obj.__class__.__name__, obj_str)
        self.assertIn(obj.id, obj_str)

if __name__ == '__main__':
    unittest.main()
