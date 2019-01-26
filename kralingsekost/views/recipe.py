import pyramid.httpexceptions as exc
from pyramid.view import view_config

from .. import models


@view_config(
    route_name='recipe.list',
    renderer='../templates/recipe/list.mako'
)
def list_(request):
    search_query = request.params.get('q', None)

    recipes = request.dbsession.query(models.Recipe)

    if search_query:
        recipes.filter(models.Recipe.name.ilike(search_query))

    return {'recipes': recipes.limit(10)}


@view_config(
    route_name='recipe.detail',
    renderer='../templates/recipe/detail.mako'
)
def detail(request):
    recipe_id = request.matchdict['recipe_id']

    recipe = request.dbsession.query(models.Recipe).get(recipe_id)

    if not recipe:
        raise exc.HTTPNotFound('Recipe not found')

    return {'recipe': recipe}
