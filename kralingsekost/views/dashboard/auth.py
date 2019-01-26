import logging
import pyramid.httpexceptions as exc
from pyramid.view import view_config
from pyramid.security import remember, forget

from kralingsekost import models
from kralingsekost.security import hash_password

log = logging.getLogger(__name__)


@view_config(
    route_name='dashboard.auth.login',
    request_method=['GET', 'POST'],
    renderer='dashboard/auth.mako'
)
def login(request):
    if request.method == 'GET':
        return {}

    try:
        email = request.POST['email']
        password = request.POST['password']
    except KeyError:
        raise exc.HTTPBadRequest()

    user = request.dbsession.query(models.User).filter_by(email=email).one()

    # TODO: FIX
    # if hash_password(password) != user.password:
    #     raise exc.HTTPUnauthorized('Wrong password')

    headers = remember(request, user.id)

    return exc.HTTPFound(
        request.route_path('dashboard.recipe.list'),
        headers=headers
    )


@view_config(route_name='dashboard.auth.logout')
def logout(request):
    headers = forget(request)
    url = request.route_url('recipe.list')
    return exc.HTTPFound(
        location=url,
        headers=headers
    )
