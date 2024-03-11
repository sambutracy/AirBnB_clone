#!/usr/bin/python3
""" Amenity class module """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.

    Attributes:
        name (str): The name of the Amenity.
    """
    name = ""
