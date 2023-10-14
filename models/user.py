#!/usr/bin/python3
"""Define User class that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """BaseModel is the base class for the project's data model.
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
