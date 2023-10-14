#!/usr/bin/python3
"""Define Review class that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """BaseModel is the base class for the project's data model.
    """
    place_id = ''
    user_id = ''
    text = ''
