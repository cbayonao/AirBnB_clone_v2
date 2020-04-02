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
    2. Private class attributes:
    __engine: set to None
    __session: set to None
    3. Public instance methods:
    __init__(self):
    """
    __engine = None
    __session = None
    models = {User, State, City, Amenity, Place, Review}

    def __init__(self):
        """
        4. all of the following values must be retrieved via
        environment variables:
        MySQL user: HBNB_MYSQL_USER
        MySQL password: HBNB_MYSQL_PWD
        MySQL host: HBNB_MYSQL_HOST (here = localhost)
        MySQL database: HBNB_MYSQL_DB
        don’t forget the option pool_pre_ping=True when you call create_engine
        drop all tables if the environment variable HBNB_ENV is equal to test
        5. create the engine (self.__engine)
        the engine must be linked to the MySQL database and user created
        before (hbnb_dev and hbnb_dev_db):
        dialect: mysql
        driver: mysqldb
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
        6. all(self, cls=None):
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        if cls=None, query all types of objects (User, State, City,
        Amenity, Place and Review)
        this method must return a dictionary: (like FileStorage)
        key = <class-name>.<object-id>
        value = object
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
        7. new(self, obj): add the object to the current
        database session (self.__session)
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        8. save(self): commit all changes of the current
        database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        9. delete(self, obj=None): delete from the current
        database session obj if not None.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        10. reload(self):
        create all tables in the database (feature of SQLAlchemy)
        (WARNING: all classes who inherit from Base must be imported before
        calling Base.metadata.create_all(engine))
        create the current database session (self.__session) from the engine
        (self.__engine)
        by using a sessionmaker - the option expire_on_commit must be set to
        False;
        and scoped_session to make sure your Session is thread-safe
        """
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()