import sqlite3
import logging
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class Repository():
    """ Repository """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.engine = create_engine('sqlite:///test.db', echo=True)
        self.sessionFactory = sessionmaker(bind=self.engine)

    def __enter__(self):
        self.logger.debug("Getting session")
        self.session = self.sessionFactory()
        return self.session

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.logger.debug("Rollbacking session")
            self.session.rollback()
        self.logger.info("Clossing session")
        self.session.close()
        return False
