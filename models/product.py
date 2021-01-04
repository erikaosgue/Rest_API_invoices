

""" Module that contains the Product class """

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer


class Product(BaseModel, Base):
    """ Class Priduct """

    __tablename__ = 'products'
    description = Column(String(128), nullable=False)
    product_code = Column(Integer, nullable=False)