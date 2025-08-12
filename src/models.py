from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Float, Integer, Column, Table, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

Favorites_character = Table(
    "favorites_character",
    db.Model.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("character_id", ForeignKey("character.id"), primary_key=True)
)

Favorites_vehicle = Table(
    "favorites_vehicle",
    db.Model.metadata,
    Column("user.id", ForeignKey("user.id"), primary_key=True),
    Column("vehicle_id", ForeignKey("vehicle.id"), primary_key=True)
)

Favorites_planet = Table(
    "favorites_planet",
    db.Model.metadata,
    Column("user.id", ForeignKey("user.id"), primary_key=True),
    Column("planet.id", ForeignKey("planet.id"), primary_key=True),
)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    id: Mapped [int] = mapped_column(primary_key=True)
    name: Mapped [str] = mapped_column(String(20), nullable=False)
    gender: Mapped[str] = mapped_column(String(10), nullable=False)
    eye_color: Mapped[str] = mapped_column(String(10), nullable=False)
    mass: Mapped[float] = mapped_column(Float(5), nullable=False)

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "eye_color": self.eye_color,
            "mass": self.mass
        }
    
class Vehicle(db.Model):
    id: Mapped [int] = mapped_column(primary_key=True)
    name: Mapped [str] = mapped_column(String(20), nullable=False)
    passengers: Mapped[int] = mapped_column(Integer, nullable=False)
    model: Mapped[str] = mapped_column(String(10), nullable=False)

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "passengers": self.passengers,
            "model": self.model,
        }
    
class Planet(db.Model):
    id: Mapped [int] = mapped_column(primary_key=True)
    name: Mapped [str] = mapped_column(String(40), nullable=False)
    climate: Mapped [str] = mapped_column(String(20), nullable=False)
    terrain: Mapped [str] = mapped_column(String(20), nullable=False)
    gravity: Mapped [str] = mapped_column(String(20), nullable=False)

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "gravity": self.gravity,
        }