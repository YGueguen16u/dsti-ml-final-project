# back_end/database/models/activity_log.py

"""
Activity logging models.

This module defines all tables used to log physical activities performed by users.
It supports general metadata (e.g. type, intensity) as well as schema-specific structures
for sports such as muscle training and sprinting.

Tables defined:
- Activity
- MuscleTraining (1-to-1 with Activity)
- MuscleTrainingSet (linked to MuscleTraining)
- Sprint (1-to-1 with Activity)

Relationships:
- Activity → User (many-to-one)
- Activity → MuscleTraining or Sprint (one-to-one)
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Activity(Base):
    """
    General activity log entry for a user.

    Supports metadata such as:
    - type (e.g., 'muscle_training', 'sprint')
    - intensity (e.g., moderate, high)
    - moment (e.g., 'morning', 'evening')

    Specialized activity schemas (e.g., MuscleTraining, Sprint) are linked via one-to-one relationships.
    """
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False)
    type = Column(String)
    duration = Column(String)
    intensity = Column(String)
    moment = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="activities")

    # Schema specializations
    muscle_training = relationship("MuscleTraining", back_populates="activity", uselist=False)
    sprint = relationship("Sprint", back_populates="activity", uselist=False)


class MuscleTraining(Base):
    """
    Muscle training session details for a given Activity.
    One activity can include multiple exercises.

    Example:
    - Bench press: 3 sets of 10 reps, 60kg, 90s rest
    """
    __tablename__ = "muscle_trainings"
    id = Column(Integer, primary_key=True)
    activity_id = Column(ForeignKey("activities.id"), nullable=False)
    name = Column(String)

    activity = relationship("Activity", back_populates="muscle_training")
    sets = relationship("MuscleTrainingSet", back_populates="exercise", cascade="all, delete-orphan")


class MuscleTrainingSet(Base):
    """
    A single set within a muscle training exercise.

    Fields:
    - reps: number of repetitions
    - weight: amount lifted (e.g., '60kg')
    - rest: rest time after the set (e.g., '90s')
    """
    __tablename__ = "muscle_training_sets"
    id = Column(Integer, primary_key=True)
    exercise_id = Column(ForeignKey("muscle_trainings.id"), nullable=False)
    reps = Column(Integer)
    weight = Column(String)
    rest = Column(String)

    exercise = relationship("MuscleTraining", back_populates="sets")


class Sprint(Base):
    """
    Sprint training details for a given Activity.

    One-to-one relationship with the base Activity.

    Fields:
    - distance (e.g., '100m')
    - time (e.g., '10s')
    - rest (e.g., '5min')
    """
    __tablename__ = "sprints"
    id = Column(Integer, primary_key=True)
    activity_id = Column(ForeignKey("activities.id"), nullable=False)
    distance = Column(String)
    time = Column(String)
    rest = Column(String)

    activity = relationship("Activity", back_populates="sprint")