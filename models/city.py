#!/usr/bin/python3
"""Define City class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """BaseModel is the base class for the project's data model.
    """
    state_id = ""
    name = ""
