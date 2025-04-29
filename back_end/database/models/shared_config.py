# back_end/database/models/shared_config.py

"""
Shared configuration tables used across the application.

These tables store fixed reference values for:
- Gender (e.g., Male, Female, Other)
- Diet Type (e.g., Vegetarian, Vegan, Omnivore)
- Fitness Level (e.g., Beginner, Intermediate)
- Goal (e.g., Lose weight, Gain muscle)

These tables are normalized and used via foreign keys to ensure consistency.
"""

from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

# Many-to-many association between users and their goals
user_goals = Table(
    "user_goals",
    Base.metadata,
    Column("user_id", String, ForeignKey("users.user_id"), primary_key=True),
    Column("goal_id", Integer, ForeignKey("goals.goal_id"), primary_key=True)
)


class Gender(Base):
    """
    Reference table listing all possible genders (e.g., male, female, other).
    """
    __tablename__ = "genders"

    id = Column(Integer, primary_key=True)
    label = Column(String(50), unique=True, nullable=False)


class DietType(Base):
    """
    Reference table listing types of diets (e.g., vegan, keto, omnivore).
    """
    __tablename__ = "diet_types"

    id = Column(Integer, primary_key=True)
    label = Column(String, unique=True, nullable=False)


class FitnessLevel(Base):
    """
    Reference table listing fitness levels (e.g., beginner, intermediate, advanced).
    """
    __tablename__ = "fitness_levels"

    id = Column(Integer, primary_key=True)
    label = Column(String, unique=True, nullable=False)


class Goal(Base):
    """
    Reference table listing personal user goals (e.g., 'Gain muscle', 'Lose weight').
    """
    __tablename__ = "goals"

    goal_id = Column(Integer, primary_key=True)
    label = Column(Text, unique=True, nullable=False)
