
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Date, Integer
from datetime import datetime
from sqlalchemy.orm import relationship

""" Module that creates the Invoice object """

class Invoice(BaseModel, Base):
    """ Class Invoice """

    __tablename__ = 'invoices'
    invoice_number = Column(String(10), nullable=False)
    date = Column(Date, nullable=True)
    client_id = Column(String(60), ForeignKey('clients.id'), nullable=False)
    client_name = Column(String(60), nullable=False)
    discount = Column(Integer, nullable=False)
    items = relationship("Item", backref="invoices", cascade="all, delete, delete-orphan")
    subtotal = Column(Integer, nullable=True, default=0)
    total = Column(Integer, nullable=True, default=0)
    num_items = Column(Integer, nullable=True, default=0)
