import os
import uuid
import shutil
import pyramid.httpexceptions as exc
from pyramid.view import view_config

from wtforms import (
    Form, StringField, validators, SelectField, FieldList, FormField)
from kralingsekost import models


class IngredientForm(Form):
    name = StringField('name', [
        validators.InputRequired()
    ])
    amount = StringField('amount', [
        validators.InputRequired()
    ])

class RecipeForm(Form):
    name = StringField('name', [
        validators.InputRequired()
    ])
    description = StringField('description', [
        validators.InputRequired()
    ])
    image_url = StringField('image_url', [
        validators.InputRequired()
    ])
    category_id = SelectField('Category', [
        validators.InputRequired()
    ], coerce=int)

    ingredients = FieldList(FormField(IngredientForm))



@view_config(
    route_name='dashboard.recipe.list',
    renderer='dashboard/list.mako',
    permission='private'
)
def list_(request):
    search_query = request.params.get('q', None)

    # You can only see your own recipes in the dashboard
    recipes = request.dbsession.query(models.Recipe).filter_by(
        author_id=request.user.id
    )

    if search_query:
        recipes.filter(models.Recipe.name.ilike(search_query))

    return {'recipes': recipes.limit(10)}


@view_config(
    route_name='dashboard.recipe.edit', 
    renderer='dashboard/edit.mako',
    permission='private'
)
def edit(request):
    recipe_id = request.matchdict['recipe_id']
    recipe = request.dbsession.query(models.Recipe).get(recipe_id)

    if not recipe:
        raise exc.HTTPNotFound('Recipe not found')

    if recipe.author_id != request.user.id:
        raise exc.HTTPUnauthorized('You can only edit your own recipes')

    form = RecipeForm(request.POST, recipe)
    categories = request.dbsession.query(models.Category).all()
    form.category_id.choices = [(c.id, c.name) for c in categories]
    
    if request.method == 'POST' and form.validate():
        form.populate_obj(recipe)
        request.dbsession.add(recipe)
        return exc.HTTPFound(
            request.route_path('dashboard.recipe.list')
        )

    return {
        'form': form,
        'recipe': recipe
    }


@view_config(
    route_name='dashboard.recipe.create',
    renderer='dashboard/create.mako',
    permission='private'
)
def create(request):
    form = RecipeForm(request.POST)
    categories = request.dbsession.query(models.Category).all()
    form.category_id.choices = [(c.id, c.name) for c in categories]

    if request.method == 'POST' and form.validate():
        recipe = models.Recipe()
        recipe.name = form.name.data
        recipe.description = form.description.data
        recipe.image_url = form.image_url.data
        recipe.category_id = form.category_id.data
        recipe.author = request.user
        request.dbsession.add(recipe)

        return exc.HTTPFound(
            request.route_path('dashboard.recipe.list')
        )

    return {
        'form': form
    }


@view_config(
    route_name='dashboard.recipe.delete',
    permission='private'
)
def delete(request):
    recipe_id = request.matchdict['recipe_id']
    recipe = request.dbsession.query(models.Recipe).get(recipe_id)

    request.dbsession.delete(recipe)
    return exc.HTTPFound(
        request.route_path('dashboard.recipe.list')
    )
