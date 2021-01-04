
""" Module that contains the class Client """

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String


class Client(BaseModel, Base):
    """ Class client """

    __tablename__ = 'clients'
    name = Column(String(128), nullable=False)
