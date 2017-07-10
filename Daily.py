import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shop(Base):
    __tablename__ = 'shop'
    name = Column(String(80), nullable = False);
    id = Column(Integer, primary_key = True);



class Daily(Base):
    __tablename__ = 'daily'
    name = Column(String(80),nullable = False);
    id = Column(Integer, primary_key = True);
    item = Column(String(250));
    price = Column(String(8));
    shop_id = Column(Integer, ForeignKey('shop.id'));
    shop = relationship(Shop);


engine = create_engine('sqlite:///shop.db')

Base.metadata.create_all(engine)

