# back_end/database/models/base.py

"""
Base declarative class for all SQLAlchemy models.

This module defines the common SQLAlchemy `Base` class used to declare all ORM models
in the project. It serves as the metadata registry and foundational base for model definitions.

Usage:
    All ORM classes should inherit from this base:

        from .base import Base

        class MyModel(Base):
            __tablename__ = "my_table"
            ...

Why use a centralized Base?
----------------------------
- Ensures all models share the same metadata (`Base.metadata`)
- Allows for unified schema creation with `Base.metadata.create_all(bind=engine)`
- Encourages modular model definitions in separate files

Example:
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()
"""

from sqlalchemy.orm import declarative_base

Base = declarative_base()