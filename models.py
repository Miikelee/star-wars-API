from flask_sqlalchemy import SQLAlchemy
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
db = SQLAlchemy()

class User(db.Model):
   __tablename__ = 'user'
   id = db.Column(Integer, primary_key=True)
   username = db.Column(db.String(25), unique=True, nullable=False)
   first_name = db.Column(db.String(25), nullable=False)
   last_name = db.Column(db.String(25), nullable=False)
   email = db.Column(db.String(30),unique=True, nullable=False) 
   password= db.Column(db.String(12), nullable=False)

   def __repr__(self):
        return "<User %r>" % self.id
    
   def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name, 
            'last_name': self.last_name,
            'password': self.password,
            'email': self.email
        }
    
   def serialize_just_username(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name, 
            'last_name': self.last_name,
            'password': self.password,
            'email': self.email
        }


class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    vehicle_class = db.Column(db.String (250))
    cargo_capacity = db.Column(db.Integer)
    #characters = relationship('Characters')
    #characters_id = Column(Integer, ForeignKey('characters.id'))

    def __repr__(self):
        return "<Vehicles %r>" % self.id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model, 
            'cargo_capacity': self.cargo_capacity, 
            'vehicle_class': self.vehicle_class
        }

    def serialize_just_username(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model, 
            'cargo_capacity': self.cargo_capacity, 
            'vehicle_class': self.vehicle_class
        }


class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    mass = db.Column(db.Integer)
    #planets = relationship('Planets')
    #homeworld_id = Column(Integer, ForeignKey('planets.id'))
    #vehicles = relationship('Vehicles')
    #vehicles_id = Column(Integer, ForeignKey('vehicles.id'))

    def __repr__(self):
        return "<Characters %r>" % self.id

    def serialize(self):

        return {
            'id': self.id,
            'name': self.name,
            'mass': self.mass, 
            'eye_color': self.eye_color,  
            'gender': self.gender
            
        }

    def serialize_just_username(self):

        return {
            'id': self.id,
            'name': self.name,
            'mass': self.mass, 
            'eye_color': self.eye_color, 
            'gender': self.gender
            
            
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    climate = db.Column(db.String(200))
    terrain = db.Column(db.String(200))
    diameter= db.Column(db.Integer)

    def __repr__(self):
        return "<Planets %r>" % self.id

    def serialize(self): 
        return {
            'id': self.id,
            'name': self.name,
            'climate': self.climate,
            'terrain': self.terrain,
            'diameter': self.diameter
        }

    def serialize_just_username(self): 
        return {
            'id': self.id,
            'name': self.name,
            'climate': self.climate,
            'terrain': self.terrain,
            'diameter': self.diameter
        }

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    favorite_planets = db.relationship('Planets')
    favorite_planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    favorite_vehicles = db.relationship('Vehicles')
    favorite_vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    favorite_characters = db.relationship('Characters')
    favorite_characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))

    def __repr__(self):
        return '<Favorites %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets_id": self.planets_id,
            "characters_id": self.characters_id,
            "vehicles_id": self.vehicles_id
        }
    
    def serialize_just_username(self): 
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets_id": self.planets_id,
            "characters_id": self.characters_id,
            "vehicles_id": self.vehicles_id
        }