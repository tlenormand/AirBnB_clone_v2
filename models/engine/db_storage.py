#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import Session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """This class manages storage of hbnb models in DB format"""
    __engine = None
    __session = None

    def __init__(self):
        """Instatntiates a new engine"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB")
            ),
            pool_pre_ping=True
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        self.__session = Session(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name
        """
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        classes = [User, Place, State, City, Amenity, Review]
        dictionary = {}
        if cls:
            for obj in self.__session.query(cls).all():
                dictionary[f"{obj.__class__.__name__}.{obj.id}"] = obj
        else:
            for item in classes:
                for obj in self.__session.query(item).all():
                    dictionary[f"{obj.__class__.__name__}.{obj.id}"] = obj

        if hasattr(dictionary, "_sa_instance_state"):
            del dictionary["_sa_instance_state"]

        return dictionary

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        sessionmaked = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sessionmaked)
