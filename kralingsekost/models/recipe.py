from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    ForeignKey,
    Boolean
)
from sqlalchemy.orm import relationship

from .meta import Base


class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)

    name = Column(String)
    description = Column(Text)
    slug = Column(String, unique=True)

    hidden = Column(Boolean, default=False)

    image_url = Column(String)

    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship('User', back_populates='recipes')

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category')

    ingredients = relationship('Ingredient')


class Ingredient(Base):
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(String)

    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    recipe = relationship('Recipe')


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String)
