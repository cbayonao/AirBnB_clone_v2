#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    place_id = ""
    user_id = ""
    text = ""
