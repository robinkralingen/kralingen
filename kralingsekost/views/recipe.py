import pyramid.httpexceptions as exc
from pyramid.view import view_config
from sqlalchemy import or_
from .. import models


@view_config(
    route_name='recipe.list',
    renderer='../templates/recipe/list.mako'
)
def list_(request):
    search_query = request.params.get('q', None)
    category = request.params.get('category', None)

    recipes = request.dbsession.query(models.Recipe).filter_by(hidden=False)

    if search_query:
        recipes = recipes.filter(or_(
            models.Recipe.name.ilike('%'+search_query+'%'),
            models.Recipe.description.ilike('%'+search_query+'%')
        ))
    
    if category:
        recipes = recipes.filter(models.Recipe.category_id == category)

    categories = request.dbsession.query(models.Category).all()

    return {
        'recipes': recipes.limit(10),
        'categories': categories
    }


@view_config(
    route_name='recipe.detail',
    renderer='../templates/recipe/detail.mako'
)
def detail(request):
    recipe_id = request.matchdict['recipe_id']

    recipe = request.dbsession.query(models.Recipe).get(recipe_id)

    if not recipe or recipe.hidden:
        raise exc.HTTPNotFound('Recipe not found')

    return {'recipe': recipe}
