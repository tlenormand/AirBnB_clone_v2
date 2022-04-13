#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City",
            backref="State",
            cascade="all, delete-orphan"
        )
    else:
        name = ""

        @property
        def get_cities(self):
            """
            returns the list of City instances with state_id equals
            to the current State.id
            """
            listCity = []
            for k in storage.__object:
                if (k["__class__"] == "City") and k["state_id"] == self.id:
                    listCity.append(k)
            return listCity
