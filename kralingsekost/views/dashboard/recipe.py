import os
import uuid
import shutil
import pyramid.httpexceptions as exc
from pyramid.view import view_config

from kralingsekost import models


@view_config(route_name='dashboard.recipe.list', renderer='dashboard/list.mako')
def list_(request):
    search_query = request.params.get('q', None)

    # You can only see your own recipes in the dashboard
    recipes = request.dbsession.query(models.Recipe).filter_by(
        author_id=request.user.id
    )

    if search_query:
        recipes.filter(models.Recipe.name.ilike(search_query))

    return {'recipes': recipes.limit(10)}


@view_config(route_name='dashboard.recipe.edit', renderer='dashboard/edit.mako')
def edit(request):
    recipe_id = request.matchdict['recipe_id']

    if request.method == 'POST':
        recipe = request.dbsession.query(models.Recipe).get(recipe_id)
        recipe.name = request.POST.get('name')
        recipe.description = request.POST.get('description')
        request.dbsession.add(recipe)
        return exc.HTTPFound(
            request.route_path('dashboard.recipe.list')
        )


    recipe = request.dbsession.query(models.Recipe).get(recipe_id)

    if recipe.author_id != request.user.id:
        raise exc.HTTPUnauthorized('You can only edit your own recipes')

    if not recipe:
        raise exc.HTTPNotFound('Recipe not found')

    return {'recipe': recipe}


@view_config(route_name='dashboard.recipe.create', renderer='dashboard/create.mako')
def create(request):
    if request.method == 'GET':
        return {}
    # Create recipe from request.POST

    recipe = models.Recipe()
    recipe.name = request.POST.get('name')
    recipe.description = request.POST.get('description')
    recipe.author = request.user

    request.dbsession.add(recipe)

    return exc.HTTPFound(
        request.route_path('dashboard.recipe.list')
    )

    # def save_file(file_object):
    #     input_file = file_object.file
    #     target_filename = '%s.jpg' % uuid.uuid4()

    #     file_path = os.path.join(
    #         request.registry.settings['upload_dir'],
    #         target_filename
    #     )

    #     temp_file_path = file_path + '~'

    #     input_file.seek(0)
    #     with open(temp_file_path, 'wb') as output_file:
    #         shutil.copyfileobj(input_file, output_file)

    #     os.rename(temp_file_path, file_path)
    #     return target_filename

    # # If not all required information is present -> Return errors

    # # If recipe is successfully created -> redirect to overview


@view_config(route_name='dashboard.recipe.delete')
def delete(request):
    recipe_id = request.matchdict['recipe_id']
    recipe = request.dbsession.query(models.Recipe).get(recipe_id)

    request.dbsession.delete(recipe)
    return exc.HTTPFound(
        request.route_path('dashboard.recipe.list')
    )
