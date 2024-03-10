#!/usr/bin/python3
""" Doc Here """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
# from models.base_model import BaseModel #avoid circular


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects. """
        return FileStorage.__objects

    def new(self, obj):
        """set in __objects obj with key """
        id = obj.to_dict().["id"]
        className = obj.to_dict()["__class__"]
        keyName = className+"."+id
        FileStorage.__objects[keyName] = obj

    def save(self):
        """ Serialize __objects to the JSON file __file_path """
        filepath = FileStorage.__file_path
        data = dict(FileStorage.__objects)
        for key, value in data.items():
            data[key] = value.to_dict()
        with open(filepath, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """ Reload objects from JSON file into __objects dictionary """
        filepath = FileStorage.__file_path
        data = FileStorage.__objects
        if os.path.exists(filepath):
            try:
                with open(filepath) as f:
                    for key, value in json.load(f).items():
                        if "BaseModel" in key:
                            data[key] = BaseModel(**value)
                        if "User" in key:
                            data[key] = User(**value)
                        if "Place" in key:
                            data[key] = Place(**value)
                        if "State" in key:
                            data[key] = State(**value)
                        if "City" in key:
                            data[key] = City(**value)
                        if "Amenity" in key:
                            data[key] = Amenity(**value)
                        if "Review" in key:
                            data[key] = Review(**value)
            except Exception:
                pass
