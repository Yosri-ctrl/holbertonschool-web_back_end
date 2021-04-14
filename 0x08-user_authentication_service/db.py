#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add_user to User database
        """
        u = User(email=email, hashed_password=hashed_password)
        self._session.add(u)
        self._session.commit()
        return u

    def find_user_by(self, **kwargs) -> User:
        """ find user by keywords in kwargs
        """
        user = self._session.query(User).filter_by(**kwargs)
        if user is None:
            raise NoResultFound
        if kwargs is None:
            raise InvalidRequestError
        return user.one()

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update the User database using the find_user_by
        """
        u = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(u, key):
                raise ValueError
            setattr(u, key, value)
        self._session.add(u)
        self._session.commit()
