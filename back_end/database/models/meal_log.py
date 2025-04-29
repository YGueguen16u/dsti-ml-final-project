# back_end/database/models/meal_log.py

"""
Meal logging models.

This module defines the tables required to log user meals, their composition,
and the context (meal time, label, etc.).

Tables defined:
- Meal
- MealFood

Relationships:
- Meal → User (many-to-one)
- Meal → MealFood (one-to-many)
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Meal(Base):
    """
    A recorded meal consumed by a user.

    Fields:
    - label: Name of the meal (e.g., 'breakfast', 'dinner')
    - time: Time of the meal (e.g., '8am')
    - created_at: Timestamp when the entry was created
    """
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.user_id"), nullable=False)
    label = Column(String)
    time = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="meals")
    foods = relationship("MealFood", back_populates="meal", cascade="all, delete-orphan")


class MealFood(Base):
    """
    A food item part of a Meal.

    Fields:
    - food: Name of the food (e.g., 'banana')
    - quantity: Quantity consumed (e.g., '200g', '1 bowl')
    - reference: Optional brand or food reference (e.g., 'Bjorg')
    """
    __tablename__ = "meal_foods"

    id = Column(Integer, primary_key=True)
    meal_id = Column(ForeignKey("meals.id"), nullable=False)
    food = Column(String)
    quantity = Column(String)
    reference = Column(String)

    meal = relationship("Meal", back_populates="foods")