import sqlite3
import logging

class Repository():
    """ SQLlite3 repository """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)    

    def __enter__(self):
        self.logger.debug("Getting db connection")
        self.db = sqlite3.connect('test.db')
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.logger.debug("Closing db connection")
        self.db.close()
        return False
    