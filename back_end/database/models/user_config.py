# back_end/database/models/user_config.py

"""
User configuration models.

This module defines the main user profile table only.
Reference tables (Gender, DietType, FitnessLevel, Goal) are imported from shared_catalog.py.

Table defined:
- User (linked to shared reference tables via foreign keys)

Relationships:
- User → Gender, DietType, FitnessLevel (many-to-one)
- User → Goals (many-to-many via association table user_goals)
"""

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from back_end.database.models.shared_config import Gender, DietType, FitnessLevel, Goal, user_goals
# from database.models.shared_config import Gender, DietType, FitnessLevel, Goal, user_goals
class User(Base):
    """
    Main user profile table.

    Stores personal data and links to user configuration choices
    via foreign keys (gender, diet, fitness level).
    Supports many-to-many relationship with goals.
    """
    __tablename__ = "users"

    user_id = Column(String, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    target_weight = Column(Float)

    gender_id = Column(Integer, ForeignKey("genders.id"), nullable=False)
    diet_type_id = Column(Integer, ForeignKey("diet_types.id"), nullable=False)
    fitness_level_id = Column(Integer, ForeignKey("fitness_levels.id"), nullable=False)

    gender = relationship("Gender", lazy="joined")
    diet_type = relationship("DietType", lazy="joined")
    fitness_level = relationship("FitnessLevel", lazy="joined")
    goals = relationship("Goal", secondary=user_goals, backref="users")

    # Activities and Meals (defined elsewhere)
    activities = relationship("Activity", back_populates="user", cascade="all, delete-orphan")
    meals = relationship("Meal", back_populates="user", cascade="all, delete-orphan")