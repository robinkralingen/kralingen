from .meta import Base

from sqlalchemy import (
    Column,
    Integer,
    String,
    Table,
    ForeignKey
)
from sqlalchemy.orm import relationship


user_roles = Table(
    'user_role', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('role_id', Integer, ForeignKey('role.id'))
)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    recipes = relationship('Recipe', back_populates='author')

    roles = relationship('Role', secondary=user_roles)


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String)
