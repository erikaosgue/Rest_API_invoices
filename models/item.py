

"""Module that creates a new item """

import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from models.base_model import Base, BaseModel

class Item(BaseModel, Base):
    """Class Item """

    __tablename__ = 'items'
    item_number = Column(String(10), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    name = Column(String(60), nullable=False)
    product_id = Column(String(60), ForeignKey('products.id'), nullable=False)
    invoice_id = Column(String(60), ForeignKey('invoices.id'), nullable=False)
    total = Column(Integer, nullable=True, default=0)