#!/usr/bin/python3
"""
 Defining the FileStorage class
"""

import json
import datetime


class FileStorage:
    """
    class FileStorage that serializes instances
    to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """dictionary of class instances"""
        return type(self).__objects

    def new(self, obj):
        """creates dictionary of class instances"""
        n_dict = {}
        n_dict[type(obj).__name__ + '.' + obj.id] = obj
        type(self).__objects.update(n_dict)

    def save(self):
        """serializes obj to JSON file"""
        from models.base_model import BaseModel
        new_dict = {}
        new_dict.update(type(self).__objects)
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        with open(type(self).__file_path, "w", encoding="utf-8") as write_file:
            json.dump(new_dict, write_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        try:
            with open(type(self).__file_path, "r", encoding="utf-8") as read_f:
                json_dict = json.load(read_f)
            for key, value in json_dict.items():
                type(self).__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            return
