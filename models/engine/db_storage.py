#!/usr/bin/python3
"""DBStorage - States and Cities"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """
    Private class attributes
    Public instance methods
    """
    __engine = None
    __session = None
    models = {User, State, City}

    def __init__(self):
        """
        all of the following values must be retrieved via
        environment variables:
        create the engine (self.__engine)
        """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, db),
                                      pool_pre_ping=True)
        if env == "test":q
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        all(self, cls=None):
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        """
        if cls:
            obj = self.__session.query(self.classes()[cls])
        else:
            obj = self.__session.query(State).all()
            obj += self.__session.query(City).all()
            obj += self.__session.query(User).all()
            obj += self.__session.query(Place).all()
            obj += self.__session.query(Amenity).all()
            obj += self.__session.query(Review).all()
        sql_dict = {}
        for o in obj:
            key = '{}.{}'.format(type(obj).__name__, o.id)
            sql_dict[key] = o
        return sql_dict

    def new(self, obj):
        """
        new(self, obj): add the object to the current
        database session (self.__session)
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        save(self): commit all changes of the current
        database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete(self, obj=None): delete from the current
        database session obj if not None.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        reload(self):
        create all tables in the database (feature of SQLAlchemy)
        """
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()
