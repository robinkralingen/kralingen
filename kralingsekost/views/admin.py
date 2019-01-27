from kralingsekost import models
from pyramid.view import view_config
import pyramid.httpexceptions as exc


@view_config(
    route_name='admin.overview',
    renderer='admin/list.mako',
    permission='administrator'
)
def overview(request):
    recipes = request.dbsession.query(models.Recipe)\
        .order_by(models.Recipe.name).all()
    return {
        'recipes': recipes
    }


@view_config(
    route_name='admin.recipe.toggle',
    renderer='admin/list.mako',
    permission='administrator'
)
def toggle(request):
    recipe_id = request.matchdict['recipe_id']
    print(recipe_id)
    recipe = request.dbsession.query(models.Recipe).get(recipe_id)
    recipe.hidden = not recipe.hidden
    return exc.HTTPFound(request.route_url('admin.overview'))
