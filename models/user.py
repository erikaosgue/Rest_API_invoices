
"""Module that creates a new User """

import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from models.base_model import Base, BaseModel

class User(BaseModel, Base):
    """Class User """

    __tablename__ = 'users'
    lastInvoiceCode = Column(Integer, nullable=True)
    lastItemCode = Column(Integer, nullable=True)
    name = Column(String(60), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Item"""
        super().__init__(*args, **kwargs)