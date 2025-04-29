# back_end/database/models.py

import datetime
from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Association Table for many-to-many relationship between users and goals
user_goals = Table(
    "user_goals",
    Base.metadata,
    Column("user_id", String, ForeignKey("users.user_id"), primary_key=True),
    Column("goal_id", Integer, ForeignKey("goals.goal_id"), primary_key=True)
)

class Gender(Base):
    __tablename__ = "genders"
    id = Column(Integer, primary_key=True)
    label = Column(String(50), unique=True, nullable=False)

class DietType(Base):
    __tablename__ = "diet_types"
    id = Column(Integer, primary_key=True)
    label = Column(String, unique=True, nullable=False)

class FitnessLevel(Base):
    __tablename__ = "fitness_levels"
    id = Column(Integer, primary_key=True)
    label = Column(String, unique=True, nullable=False)

class Goal(Base):
    __tablename__ = "goals"
    goal_id = Column(Integer, primary_key=True)
    label = Column(Text, unique=True, nullable=False)

class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    target_weight = Column(Float)

    gender_id = Column(Integer, ForeignKey("genders.id"), nullable=False)
    diet_type_id = Column(Integer, ForeignKey("diet_types.id"), nullable=False)
    fitness_level_id = Column(Integer, ForeignKey("fitness_levels.id"), nullable=False)

    gender = relationship("Gender")
    diet_type = relationship("DietType")
    fitness_level = relationship("FitnessLevel")
    goals = relationship("Goal", secondary=user_goals, backref="users")

class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.user_id"))
    type = Column(String)
    duration = Column(String)
    intensity = Column(String)
    moment = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="activities")
    muscle_training = relationship("MuscleTraining", back_populates="activity", uselist=False)
    sprint = relationship("Sprint", back_populates="activity", uselist=False)

class MuscleTraining(Base):
    __tablename__ = "muscle_trainings"
    id = Column(Integer, primary_key=True)
    activity_id = Column(ForeignKey("activities.id"))
    name = Column(String)

    activity = relationship("Activity", back_populates="muscle_training")
    sets = relationship("MuscleTrainingSet", back_populates="exercise")

class MuscleTrainingSet(Base):
    __tablename__ = "muscle_training_sets"
    id = Column(Integer, primary_key=True)
    exercise_id = Column(ForeignKey("muscle_trainings.id"))
    reps = Column(Integer)
    weight = Column(String)
    rest = Column(String)

    exercise = relationship("MuscleTraining", back_populates="sets")

class Sprint(Base):
    __tablename__ = "sprints"
    id = Column(Integer, primary_key=True)
    activity_id = Column(ForeignKey("activities.id"))
    distance = Column(String)
    time = Column(String)
    rest = Column(String)

    activity = relationship("Activity", back_populates="sprint")

class Meal(Base):
    __tablename__ = "meals"
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.user_id"))
    label = Column(String)
    time = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    foods = relationship("MealFood", back_populates="meal")
    user = relationship("User", back_populates="meals")

class MealFood(Base):
    __tablename__ = "meal_foods"
    id = Column(Integer, primary_key=True)
    meal_id = Column(ForeignKey("meals.id"))
    food = Column(String)
    quantity = Column(String)
    reference = Column(String)

    meal = relationship("Meal", back_populates="foods")