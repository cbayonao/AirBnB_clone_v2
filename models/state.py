#!/usr/bin/python3
"""This is the state class"""
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """
            Instances of cities in list
            """
            full_cities = models.storage.all(City)
            city_x_state = []
            for mycity in full_cities.values():
                if mycity.state_id == self.id:
                    city_x_state.append(mycity)
            return city_x_state
