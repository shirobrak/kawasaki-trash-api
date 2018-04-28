from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from models.database import Base
from sqlalchemy.orm import relationship
import datetime

class Trash(Base):
    __tablename__ = 'trashes'

    trash_id = Column(Integer, primary_key=True)
    name = Column(String)
    reading = Column(String)
    detail = Column(Text)
    created_at = Column(Datetime, onupdate=datetime.datetime.now)
    updated_at = Column(Datetime, onupdate=datetime.datetime.now)

    throw_rules = relationship('ThrowRule', backref="trash")

class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(Datetime, onupdate=datetime.datetime.now)
    updated_at = Column(Datetime, onupdate=datetime.datetime.now)

    throw_rules = relationship('ThrowRule', backref="category")
    collection_rules = relationship('CollectionRule', backref="category")

class Area(Base):
    __tablename__ = 'areas'

    area_id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(Datetime, onupdate=datetime.datetime.now)
    updated_at = Column(Datetime, onupdate=datetime.datetime.now)

    towns = relationship('Town', backref="area")

class Town(Base):
    __tablename__ = 'towns'

    town_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, ForeignKey('areas.area_id'))
    name = Column(String)
    created_at = Column(Datetime, onupdate=datetime.datetime.now)
    updated_at = Column(Datetime, onupdate=datetime.datetime.now)
   
    collection_rules = relationship('CollectionRule', backref="town")

class CollectionRule(Base):
    __tablename__ = 'collection_rules'

    collection_rule_id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    town_id = Column(Integer, ForeignKey('towns.town_id'))
    date = Column(Text)
    created_at = Column(Datetime, onupdate=datetime.datetime.now)
    updated_at = Column(Datetime, onupdate=datetime.datetime.now)

class ThrowRule(Base):
    __tablename__ = 'throw_rules'

    throw_rule_id = Column(Integer, primary_key=True)
    trash_id = Column(Integer, ForeignKey('trashes.trash_id'))
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    created_at = Column(Datetime, onupdate=datetime.datetime.now)
    updated_at = Column(Datetime, onupdate=datetime.datetime.now)

