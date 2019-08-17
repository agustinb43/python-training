from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from flask_jsontools import JsonSerializableBase

Base = declarative_base(cls=(JsonSerializableBase,))


class Todo(Base):

    __tablename__ = 'todos'

    def __init__(self, id, description):
        self.id = id
        self.description = description
    
    id = Column(Integer, primary_key=True)
    description = Column(String)
