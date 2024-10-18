import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum as SQLAlchemyEnum, DateTime, Float, Numeric, func 
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class CategoryType(enum.Enum):  
    PLANETS = "planet"  
    VEHICLES = "vehicle"  
    CHARACTERS = "character"   

class User(Base):
    __tablename__ = 'user'    
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), unique=True)
    created_at = Column(DateTime, server_default=func.now())
    favourites = relationship('Favourites', back_populates='user')

class Login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    user_name= Column(String(250), nullable=False, unique=True)
    password= Column(String(250), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Favourites(Base):
    __tablename__ = 'favourites'    
    id = Column(Integer, primary_key=True)
    type = Column(SQLAlchemyEnum(CategoryType), nullable=False)    
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    orbital_period = Column(Float)
    population = Column(Float)
    climate = Column(String(50))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    favourites = relationship('Favourites', back_populates='planet')

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    model = Column(String(50))
    vehicle_class = Column(String(50))
    manufacturer = Column(String(50))
    cost_in_credits = Column(Numeric(6, 2))
    length = Column(Numeric(5, 1))
    crew = Column(Float)
    passengers = Column(Float)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    favourites = relationship('Favourites', back_populates='vehicle')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    orbital_period = Column(String(50))
    population = Column(Integer)
    climate = Column(String(50))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    favourites = relationship('Favourites', back_populates='character')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
