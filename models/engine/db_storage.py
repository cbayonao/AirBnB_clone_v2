#!/usr/bin/python3
"""DBStorage - States and Cities"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """
    Private class attributes:
    __engine: set to None
    __session: set to None
    Public instance methods:
    __init__(self):
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        all of the following values must be retrieved via
        environment variables:
        drop all tables if the environment variable HBNB_ENV is equal to test
        create the engine (self.__engine)
        the engine must be linked to the MySQL database and user created
        """
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        returns a dictionary
        """
        sql_Dict = {}
        dic = ['State', 'City', 'User', 'Place', 'Review', 'Amenity']
        if cls:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                sql_Dict[key] = obj
        else:
            for model in dic:
                objects = self.__session.query(eval(model)).all()
                for obj in objects:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    sql_Dict[key] = obj
        return sql_Dict

    def new(self, obj):
        """
        new(self, obj): add the object to the current
        database session (self.__session)
        """
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
        (WARNING: all classes who inherit from Base must be imported before
        calling Base.metadata.create_all(engine))
        """
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()

    def close(self):
        self.__session.close()
